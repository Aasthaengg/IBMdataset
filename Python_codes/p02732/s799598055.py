def combination(n,r):
    n_=1
    r_=1
    for i in range(n,n-r,-1):
        n_*=i
    for i in range(1,r+1):
        r_*=i

    return n_//r_

def main():
    N=int(input())
    A=list(map(int,input().split()))

    ball_dic={}

    for a in A:
        if a in ball_dic.keys():
            ball_dic[a]+=1
        else:
            ball_dic[a]=1


    all_patern=0

    combination_dic={}

    for key in ball_dic.keys():
        if ball_dic[key]>=2:
            if (ball_dic[key] in combination_dic.keys()) is False:
                combination_dic[ball_dic[key]] = combination(ball_dic[key], 2)
            all_patern += combination_dic[ball_dic[key]]

    for a in A:
        if ball_dic[a]-1<2:
            if ball_dic[a] in combination_dic.keys():
                res=all_patern-combination_dic[ball_dic[a]]
            else:
                res=all_patern
        else:
            com=combination_dic[ball_dic[a]]
            res=all_patern-com+(com*(ball_dic[a]-2)//ball_dic[a])

        print(res)

if __name__=="__main__":
    main()