N = int(input())
T = list(map(int, input().split()))
M = int(input())

Ans = []

for _ in range(M):
    P,X = map(int, input().split())
    Ans.append(sum(T) - T[P-1] + X)

for ans in Ans:
    print(ans)