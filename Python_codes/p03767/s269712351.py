N = int(input())
a = list(map(int, input().split()))
r = 2 * N
ans = 0
a.sort(reverse=True)
if a[0] > 10**9:
    exit()
a_choiced = a[0:r][1::2]
for i in a_choiced:
    ans += i
print(ans)