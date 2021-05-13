N,K = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
result = 0
i = 0
for n in P :
    if i == K:
        break
    result+=n
    i+=1
print(result)