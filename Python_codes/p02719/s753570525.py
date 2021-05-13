n,k= list(map(int, input().strip().split()))
s=n%k
t=k-s
print(min(s,t))