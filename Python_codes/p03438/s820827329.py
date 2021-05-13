N = int(input())
a = list(map(int,(input().split())))
b = list(map(int,(input().split())))

nega = []
c = 0
gap = [0]*N
for i in range(N):
    gap[i] = a[i]-b[i]
    if gap[i] > 0:
        c += gap[i]
    elif gap[i] < 0:
        nega.append((-gap[i])//2)

nc = sum(nega)

if nc >= c:
    print("Yes")
else:
    print("No")