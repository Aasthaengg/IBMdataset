n,m=map(int, input().split())
c = 1 / (4*m)
ans = 0
l = [int(x) for x in input().split()]
l.sort(reverse=True)

for i in range(m):
    if l[i] < sum(l)*c:
        print("No")
        ans += 1
        break

if ans == 0:
    print("Yes")