N = int(input())
A = list(map(int, input().split()))
abs_A = list(map(lambda x: abs(x), A))

pos = []
neg = []
ans = 0

for e in A:
    if e > 0:
        pos.append(e)
    else:
        neg.append(e)
if len(neg) % 2 == 0:
    ans = sum(abs_A)
else:
    """pos.sort(reverse=True)
    neg.sort(reverse=True)
    if len(neg) == N:
        ans = -sum(neg[:-1]) + neg[-1]
    else:"""
    #ans = max(-sum(neg[:-1]) + neg[-1], -sum(neg[:-3]) + sum(neg[-3:]))
    #ans = max(sum(pos[:-1])-pos[-1]-sum(neg), sum(pos) + neg[0] -sum(neg[1:]))
    ans = sum(abs_A)
    ans -= 2 * min(abs_A)
print(ans)