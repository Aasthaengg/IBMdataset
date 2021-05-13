N,K = map(int,input().split())
cnt = 0
for i in range(1,N+1):
    for j in range(100):
        if i * 2**j >= K:
            cnt += 1/2**j
            break
print(cnt/N)