N, K = map(int, input().split())

list0 = []
list1 = []
set1 = set()

td = []
for i in range(N):
    t, d = map(int, input().split())
    td.append((t, d))

td.sort(key=lambda x: (x[0], -x[1]))

for t, d in td:
    if t in set1:
        list0.append(d)
    else:
        set1.add(t)
        list1.append(d)

list0.sort(reverse=True)
list1.sort(reverse=True)

various = min(K, len(list1))
selected0 = []
selected1 = []
for i in range(various):
    selected1.append(list1.pop(0))
if K > various:
    for i in range(K - various):
        selected0.append(list0.pop(0))

sum0 = sum(selected0)
sum1 = sum(selected1)
ans = sum0 + sum1 + various ** 2
while list0 and list0[0] > selected1[-1]:
    sum0 += list0.pop(0)
    sum1 -= selected1.pop(-1)
    various -= 1
    tmp = sum0 + sum1 + various ** 2
    if tmp <= ans:
        break
    ans = tmp

print(ans)
