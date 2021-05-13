N = int(input())
dic = {}
time = 0
flag = 0

for _ in range(N):
    a, b = map(int, input().split())
    if b in dic:
        dic[b] += a
    else:
        dic[b] = a

deadlines = sorted(dic.keys())

for dead in deadlines:
    time += dic[dead]
    if time > dead:
        flag += 1

if flag:
    print('No')
else:
    print('Yes')
