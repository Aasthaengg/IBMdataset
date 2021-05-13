N = int(input())
for n in range(N+1):
  if n%4==0 and (N-n)%7==0:
    print("Yes")
    break
else:
  print("No")