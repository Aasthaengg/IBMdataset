n = int(input())
A = input()
B = input()
C = input()
ans = 0
for abc in zip(A, B, C):
    ans += len(set(abc)) - 1
print(ans)
