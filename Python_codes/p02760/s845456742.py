def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

N = int(input())
for n in range(N):
  b = int(input())
  if my_index(A1, b) is not False:
    A1[my_index(A1, b)] = -1
  if my_index(A2, b) is not False:
    A2[my_index(A2, b)] = -1
  if my_index(A3, b) is not False:
    A3[my_index(A3, b)] = -1

if (sum(A1) == -3) or (sum(A2) == -3) or (sum(A3) == -3):
  print("Yes")
elif (A1[0]+A2[0]+A3[0]==-3) or (A1[1]+A2[1]+A3[1]==-3) or (A1[2]+A2[2]+A3[2]==-3):
  print("Yes")
elif (A1[0]+A2[1]+A3[2]==-3) or (A1[2]+A2[1]+A3[0]==-3):
  print("Yes")
else:
  print("No")