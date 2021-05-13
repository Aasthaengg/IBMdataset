N = input()
A, B, C = [input() for _ in range(3)]
ans = 0
for a, b, c in zip(A, B, C):
    if a == b == c:
        continue
    elif a != b and b != c and c != a:
        ans += 2
    elif a == b or b == c or c == a:
        ans += 1
print(ans)