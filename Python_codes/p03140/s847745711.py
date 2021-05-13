N = int(input())
A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

ans = 0
for z in zip(A, B, C):
    ans += len(set(z)) - 1
print(ans)
