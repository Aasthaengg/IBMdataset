N = int(input())
ListV = list(map(int, input().split()))
ListC = list(map(int, input().split()))
Sum = []
for i in range(N):
  Sum.append(ListV[i]-ListC[i])
res = 0
for i in range(N):
  if Sum[i] > 0:
    res += Sum[i]
print(res)