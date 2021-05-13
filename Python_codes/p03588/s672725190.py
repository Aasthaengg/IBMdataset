N = int(input())
mini1 = 0
mini2 = 0
for i in range(N):
  MM = input().split()
  a = int(MM[0])
  b = int(MM[1])
  if a > mini1:
    mini1 = a
    mini2 = b
    
print(mini1 + mini2)