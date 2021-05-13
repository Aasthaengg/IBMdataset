import collections

i = int(input())
li = list(map(int,input().split()))
c = collections.Counter(li)
li = list(set(li))
li.sort(reverse=True)
ans = 1
x = 0
i = 0

for i in li:
    if c[i] > 3 and x == 0:
        ans = i**2
        x += 2
    elif c[i] > 1:
        ans *= i
        x += 1
    if x == 2:
        break

if x == 2:
    print(ans)
else:
    print(0)