s=input()
t=input()
l=len(s)
for _ in range(l):
  if s==t:
    print("Yes")
    exit()
  else:
    s=s[-1]+s[:l-1]
print("No")
