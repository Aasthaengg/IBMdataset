def main():
    N=int(input())
    b=list(map(int,input().split()))
    result_inv=[]
    result_flag=True
    for _ in range(N):
        flag=False
        for i in range(len(b)):
            if i+1==b[i]:
                j=i
                flag=True
        if flag:
            a=b.pop(j)
            result_inv.append(a)
            flag=False
        else:
            result_flag=False
            break

    if result_flag:
        result=result_inv[::-1]
        for i in range(N):
            print(result[i])
    else:
        print(-1)

if __name__=="__main__":
    main()