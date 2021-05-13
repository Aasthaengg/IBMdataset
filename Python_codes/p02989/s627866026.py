n = int(input())
Ds = list(map(int, input().split()))
L1 = [0] * (10 ** 5 + 1)
L2 = [0] * (10 ** 5 + 1)
for d in Ds:
  L1[d] += 1
L2[0] = L1[0]
for i in range(1,10 ** 5 +1):
  L2[i] = L1[i] + L2[i - 1]
print(L2.count(n //2))