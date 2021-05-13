import sys
x=[int(input()) for _ in range(5)]
k=int(input())
for i in range(4):
  for j in range(i,5):
    if x[j]-x[i] > k:
      print(':(')
      sys.exit()
print('Yay!')