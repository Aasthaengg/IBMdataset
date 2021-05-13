n = int(input())
al = list(map(int, input().split()))
count = 1
ans = 0
for a in al:
    if a == count:
        count += 1
    else:
        ans += 1
if ans == len(al):
    print(-1)
else:
    print(ans)