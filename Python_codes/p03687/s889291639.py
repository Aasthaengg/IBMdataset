S = input()
ans = len(S)
for c in set(S):
    maxi = count = 0
    for s in S:
        if s != c:
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    maxi = max(maxi, count)
    ans = min(ans, maxi)
print(ans)