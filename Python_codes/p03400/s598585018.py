N = int(input())
D,X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X

for i in A:
    ans += 1 + int((D-1)/i)
    
print(ans)