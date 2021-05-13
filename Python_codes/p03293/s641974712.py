s = list(input())
t = list(input())

for i in range(len(s)):
  s = list(s[-1])+s
  s.pop()
  if s==t:
    print("Yes")
    exit()
    
print("No")