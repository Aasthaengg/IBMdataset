N = int(input())
flag = True
for i in range(100000):
  if int(i * 1.08) == N:
    print(i)
    flag = False
    break
if flag:
  print(":(")
