N = int(input())
li = []
for i in range(N):
  A = int(input())
  if A not in li:
    li.append(A)
print(len(li))