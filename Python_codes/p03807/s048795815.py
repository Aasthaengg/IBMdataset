def resolve():
    n=int(input())
    l=list(map(int, input().split()))
    cnt=0
    for i in range(n):
        if l[i]%2==1:
            cnt+=1
    if cnt%2==0:
        print('YES')
    else:
        print('NO')
resolve()