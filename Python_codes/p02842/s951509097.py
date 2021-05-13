N=int(input())
for i in range(1,500001):
    if int(i*1.08)==N:
        print(i)
        break
else:
      print(':(')
