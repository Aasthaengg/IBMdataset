n=int(input())
d=list(map(int,input().split()))
d=sorted(d)
ans=d[int(n/2)]-d[int(n/2)-1]
print(ans)