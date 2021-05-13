def sol(lis):
    m = lis[0]
    ans = []
    for i in range(len(lis)):
        if lis[i]<m:
            ans.append(m-lis[i])
            lis[i] = m
        elif  lis[i]!=m:
            m = max(m,lis[i])
    print(sum(ans))
input()
lis = list(map(int,input().split(' ')))
sol(lis)
