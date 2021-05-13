n = int(input())
s = input()
cw = 0
cb = 0
di = []
a = -1
b = 0
mn = float("inf")
for i in range(n):
    if s[i] == ".":
        cw += 1
    else:
        di.append(i)
        cb += 1
for k in range(len(di)):
    if mn > cw - di[k] + 2*k:
        mn = cw - di[k] + 2*k
print(min(min(cw,cb),mn))