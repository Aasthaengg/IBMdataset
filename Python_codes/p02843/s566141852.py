import sys
N=int(input())
a=N//105
b=N//100
for i in range(a,b+1):
  if 0<=N-i*100<=5*i:
    print("1")
    sys.exit()
print(0)