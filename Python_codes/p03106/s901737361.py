A,B,K = map(int, input().split())
C =min(A,B)
list =[]
for i in range(1,C+1):
  if A%i == 0 and B%i == 0:
    list.append(i)
list = sorted(list)
ans = list[-K]
print(ans)