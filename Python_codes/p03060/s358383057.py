n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
m=[v[i]-c[i] for i in range(n) if v[i]>c[i]]
print(sum(m))