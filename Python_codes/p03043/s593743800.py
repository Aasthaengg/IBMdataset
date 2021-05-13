N,K = list(map(int,input().split()))
out = 0
for i in range(1,N+1):
    t = 0
    now = i
    while now<K:
        now*=2
        t+=1
    out += 0.5**t
print(out/N)
