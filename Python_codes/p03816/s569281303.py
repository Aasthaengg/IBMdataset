n = int(input())
T = [int(i) for i in input().split()]
L = [0 for i in range(max(T))]

for i in range(n):
  L[T[i]-1] += 1

for i in range(len(L)):
  if L[i] >= 3:
    if L[i]%2 == 0:
    	L[i] = 2
    else:
        L[i] = 1

counttwo = L.count(2)
countone = L.count(1)

out = (counttwo//2)*2 + countone
print(out)