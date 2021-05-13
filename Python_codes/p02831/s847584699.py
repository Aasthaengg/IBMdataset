A, B = map(int, input().split())
L = max(A, B)
S = min(A, B)
ans = L
while True:
    if ans%S==0:
        print(ans)
        break
    ans+=L