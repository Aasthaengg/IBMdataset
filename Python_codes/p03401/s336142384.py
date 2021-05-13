n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
n = len(a)

iCost = [0]*(n-1)
for i in range(n-1):
    iCost[i] = abs(a[i+1]-a[i])

totCost = sum(iCost)

modCost = [0]*n # cost of when i-1th connected to i+1th point
modCost[1] = abs(a[2])
for i in range(2, n-1):
    modCost[i] = abs(a[i+1]-a[i-1])

for i in range(1, n-1):
    print(totCost - iCost[i-1] - iCost[i] + modCost[i])
