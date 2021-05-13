a = [int(i*1.08) for i in range(1, 46298)]
n = int(input())
if(n in a):
  print(a.index(n)+1)
else:
  print(":(")