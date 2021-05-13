N = int(input())
x = 0
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if A > x:
        x = A
        ans = B
print(x+ans)