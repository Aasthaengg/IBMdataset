A, B = map(int, input().split())
cake = [0]*16
for i in range(A):
  try:
    cake[i*2] = 1
  except:
    print(':(')
    exit()
for i in range(B):
  try:
    cake[(i*2)+1] = 1
  except:
    print(':(')
    exit()
print('Yay!')