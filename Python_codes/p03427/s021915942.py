N = int(input())
n = len(str(N))
NS = str(N)
ans0 = 0
for i in NS:
    ans0 += int(i)
ans1 = int(NS[0])-1 + 9 * (n-1)
ans2 = 9 * (n-1)

print(max(ans0, ans1, ans2))
