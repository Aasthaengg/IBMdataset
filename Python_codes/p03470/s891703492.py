n = int(input())
d = [int(input()) for i in range(n)]
num = [0] * 110
count = 0
for i in range(len(d)):
    num[d[i]]+= 1
for j in num:
    if j >= 1:
        count += 1
print(count)