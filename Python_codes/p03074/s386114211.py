n, k = map(int, input().split())
a = input()
l = []
if a[0] == '0':
    l.append(0)
sum = []
i = 0
while i < len(a):
    j = i
    while j < len(a) and a[j] == a[i]:
        j += 1
    l.append(j-i)
    i = j
if a[-1] == '0':
    l.append(0)
num = [0]*(len(l)+1)
for i in range(0, len(l)):
    num[i+1] = num[i]+l[i]
ans = -1
for i in range(0, len(num), 2):
    j = i + k*2+1
    if j >= len(num):
        j = len(num)-1
    ans = max(ans, num[j] - num[i])
print(ans)
