def main():
    import sys
    input = sys.stdin.readline
    N,X,Y = map(int,input().split())

    cnt_dict={}
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i==j:
                continue
            tmp1 = j-i
            tmp2 = abs(X-i)+abs(Y-j)+1
            cnt_dict[min(tmp1,tmp2)] = cnt_dict.get(min(tmp1,tmp2),0)+1

    for i in range(1,N):
        if i not in cnt_dict:
            print(0)
        else:
            print(cnt_dict[i])
            
if __name__=='__main__':
    main()