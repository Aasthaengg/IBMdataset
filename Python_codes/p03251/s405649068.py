import sys
N,M,X,Y=[int(x) for x in input().rstrip().split()]
x_n=[int(x) for x in input().rstrip().split()]
y_m=[int(x) for x in input().rstrip().split()]
x_max=max(x_n)
y_max=min(y_m)
for z in range(X+1,Y+1):
  if x_max<z and z<=y_max:
    print("No War")
    sys.exit()
print("War")
