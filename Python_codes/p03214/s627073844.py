n = int(input())
al = list(map(int, input().split()))
ave = sum(al)/n

ans = 0
ans_diff = abs(ave - al[0])
for i, a in enumerate(al):
    if abs(ave-a) < ans_diff:
        ans = i
        ans_diff = abs(ave-a)
print(ans)
