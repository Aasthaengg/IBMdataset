import sys
n=int(input())
for i in range(1, 50001):
  if i*1.08//1==n:
    print(i)
    sys.exit()
print(':(')