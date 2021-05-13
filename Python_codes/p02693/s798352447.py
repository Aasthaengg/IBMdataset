K = int(input())
tmp = input().split(" ")
A = int(tmp[0])
B = int(tmp[1])

if A + K - A % K <= B or A % K == 0:
  print("OK")
else:
  print("NG")