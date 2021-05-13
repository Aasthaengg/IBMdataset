#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

l = [int(input()) for _ in range(5)]

idx = -1
mi = 10

for i in range(5):
    remain = l[i] % 10
    if remain != 0:
        if mi > remain:
            mi = remain
            idx = i
ans = 0
for i in range(5):
    remain = l[i] % 10
    if (remain == 0):
        ans += l[i]
    else:
        if (i == idx):
            ans += l[i]
        else:
            ans += (l[i] // 10 + 1)*10
print(ans)


