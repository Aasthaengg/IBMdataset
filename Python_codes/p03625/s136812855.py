from collections import Counter

N = int(input())
A = list(map(int,input().split()))
c = Counter(A)
sticks = []
for i in c:
    s = c[i]
    if s >= 4:
        sticks.append(i)
    if s >= 2:
        sticks.append(i)
if len(sticks) < 2:
    print(0)
else:
    sticks.sort(reverse=True)
    print(sticks[0]*sticks[1])
 




