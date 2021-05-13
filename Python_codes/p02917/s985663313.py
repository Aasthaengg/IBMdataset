N = int(input())
B = list(map(int, input().split()))

B.append(-1)
b_ = B[0]
ans = 0
for b in B:
    if b < 0:
        ans += b_
    else:
        ans += min(b, b_)
        b_ = b
print(ans)