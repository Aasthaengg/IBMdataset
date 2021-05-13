mn = input().split()
ob = input().split()

n = int(mn[0])
m = int(mn[1])

votes = 0

for i in range(n):
    ob[i] = int(ob[i])
    votes += ob[i]

ob.sort(reverse = True)

line = votes/4/m

ans = 0

for i in range(m):
    if ob[i] < line:
        ans += 1

if ans == 0:
    print("Yes")
else:
    print("No")