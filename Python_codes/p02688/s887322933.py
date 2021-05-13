N,K = map(int,input().split())
a = [list(map(int,input().split())) for i in range(2*K)]
s = []; t = 0
for i in range(K):
    s = s + a[2*i+1]
for i in range(1,N+1):
    if i not in s:
        t+=1
print(t)