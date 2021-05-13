n = int(input())
l = list(input().split())
l.sort(key=int)
tmp = 0
for i in range(n - 1):tmp += int(l[i])
if int(l[n - 1]) < tmp:print("Yes")
else:print("No")