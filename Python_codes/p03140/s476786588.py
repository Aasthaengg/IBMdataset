n = input()
A = list(input())
B = list(input())
C = list(input())

ans = 0
for a, b, c in zip(A, B, C):
    if len(set([a, b, c])) == 3:
        ans += 2
    elif len(set([a, b, c])) == 2:
        ans += 1

print(ans)
