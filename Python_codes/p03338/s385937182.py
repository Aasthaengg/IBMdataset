n = int(input())
s = input()

ans = 0

for i in range(n-1):
    left = s[0:i]
    right = s[i:n]

    sleft = set([x for x in left])
    sright = set([x for x in right])

    tmp = len(sleft & sright)
    if tmp > ans:
        ans = tmp

print(ans)
