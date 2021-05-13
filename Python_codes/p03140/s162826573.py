N = int(input())
A = input()
B = input()
C = input()

ans = 0
for a, b, c in zip(A, B, C):
    if a != b and b != c and c != a:
        ans += 2
    elif a == b and b == c and c == a:
        pass
    else:
        ans += 1

print(ans)