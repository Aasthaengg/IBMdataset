N = int(input())
ans_flag = False
for i in range(N):
  a = int(input())
  if not a%2==0:
    ans_flag = True
    break

if ans_flag:
  print("first")
else:
  print("second")