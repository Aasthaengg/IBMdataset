n = [int(w) for w in input().split()]

ans = 0
if any([w % 2 == 0 for w in n]):
    ans = 0
else:
    n.sort()
    ans = (n[0]*n[1])


print(ans)
