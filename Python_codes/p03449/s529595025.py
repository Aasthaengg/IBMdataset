n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
a2.reverse()

asum1 = []
asum2 = []
tmp1 = 0
tmp2 = 0
for i in range(n):
    tmp1 += a1[i]
    asum1.append(tmp1)
    tmp2 += a2[i]
    asum2.append(tmp2)

asum2.reverse()
asum = [x + y for (x, y) in zip(asum1, asum2)]

print(max(asum))