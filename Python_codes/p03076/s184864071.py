from sys import stdin
def main():
    #入力
    readline=stdin.readline
    li=[int(readline()) for _ in range(5)]

    res=10
    res_i=0
    for i in range(5):
        if li[i]%10==0:
            pass
        else:
            if li[i]%10<res:
                res=li[i]%10
                res_i=i

    ans=0
    for i in range(5):
        if i!=res_i:
            if li[i]%10==0:
                ans+=li[i]
            else:
                ans+=li[i]+10-li[i]%10

        else:
            ans+=li[i]

    print(ans)

if __name__=="__main__":
    main()