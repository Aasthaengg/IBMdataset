def main():
    N=int(input())
    flag=0
    tmp=0
    a=0
    for tmp in range(1,1000):
        if tmp*(tmp-1)//2==N:
            flag=1
            break
    if flag==0:
        print('No')
        exit()
    else:
        print('Yes')
        print(tmp)
    lst=[[]]*tmp
    for i in range(1,tmp):
        for j in range(i):
            a+=1
            lst[i]=lst[i]+[str(a)]
            lst[j]=lst[j]+[str(a)]
    for i in range(tmp):
        print(tmp-1, " ".join(lst[i]))

main()
