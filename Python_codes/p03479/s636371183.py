X,Y = map(int,input().split())
i = 1
while Y >= X*(2**(i-1)):
  i += 1
print(i-1)