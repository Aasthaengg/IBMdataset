A=int(input())
N=1
for i in range(A+1):
  if i**2 <= A:
    N = i**2
  else:
    break
print(N)