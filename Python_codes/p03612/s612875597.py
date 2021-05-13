n = int(input())
lis = list(map(int, input().split()))

su = [0]
for i,x in enumerate(lis):
    if i == x - 1:
        su[-1] += 1
    else:
        su.append(0)

res = 0
for j in su:
    res += (j + 1)//2
print(res)
