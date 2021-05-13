N=int(input())
A=list(map(int,input().split()))
p=True
for a in A:
  if a%2==0:
    if not (a%3==0 or a%5==0):
      p=False
      break
print("APPROVED" if p else "DENIED")