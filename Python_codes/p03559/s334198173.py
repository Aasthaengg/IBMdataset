n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

li = []
i = 0
for bb in b:
    while i<n and a[i]<bb:
        i += 1
    li.append(i)
li2 = [0]
accu = 0
for i in li:
    accu += i
    li2.append(accu)
ans = 0
i = 0
for cc in c:
    while i<n and b[i]<cc:
        i += 1
    ans += li2[i]
print(ans)