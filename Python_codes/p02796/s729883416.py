n = int(input())
ls = [(0, 0)] * n
for i in range(n):
    x, ln = map(int, input().split())
    l = x - ln
    r = x + ln
    ls[i] = (l, r)
#print(ls)

ls.sort(key=lambda x: x[1])
#print(ls)
last = -float('inf')
count = 0
for i in ls:
    if last <= i[0]:
        count += 1
        last = i[1]
print(count)