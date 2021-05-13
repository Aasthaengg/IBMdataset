n,m=map(int, input().split())
a_list=[int(i) for i in input().split()]

ans=n-sum(a_list)

if ans<0:
    print(-1)
else:
    print(ans)