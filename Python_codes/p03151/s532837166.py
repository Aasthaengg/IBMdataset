n = int(input())
alis = list(map(int, input().split()))
blis = list(map(int, input().split()))

s = 0
num = 0
for i in range(n):
    if blis[i] - alis[i] > 0:
        s += blis[i] - alis[i]
        num += 1

if num == 0:
    print(0)
    exit()

nlis = []
for i in range(n):
    if alis[i]-blis[i] >= 0:
        nlis.append(alis[i]-blis[i])

nlis.sort(reverse=True)
tmp = 0
cnt = 0
for i in nlis:
    if tmp >= s:
        break
    tmp += i
    cnt += 1

if tmp < s:
    print(-1)
else:
    print(cnt+num)
