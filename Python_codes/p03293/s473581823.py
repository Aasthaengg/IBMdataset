s = input()
t = input()

n = 0
m = len(s)
while n != m:
  if s == t:
    print("Yes")
    exit()
  s = s[-1]+s[:m-1]
  n += 1
print("No")