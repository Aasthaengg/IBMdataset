X=int(input())
for i in range(int((2*X)**0.5)-2,10**9):
  if 2*X<=i*(i+1):
    print(i)
    break
