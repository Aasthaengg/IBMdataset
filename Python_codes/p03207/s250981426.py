arrp = []
N = int(input())

for i in range(0,N):
  p = int(input())
  arrp.append(p)
print(int(-0.5*max(arrp)+sum(arrp)))
