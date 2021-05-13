N,M,C = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for _ in range(N):
    A = list(map(int, input().split()))

    score = 0
    for a,b in zip(A,B):
        score += a*b
    
    if score + C > 0:
        ans += 1

print(ans)