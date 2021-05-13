N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
carry = 0
for a, b in zip(A, B):
    a2 = max(0, a - carry)

    if a2 < b:
        ans += a
        carry = b - a2
    else:
        ans += carry + b
        carry = 0

ans += min(carry, A[-1])
print(ans)