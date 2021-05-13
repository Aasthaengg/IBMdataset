n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
ans=sum(a[::2])-sum(a[1::2])
print(ans)