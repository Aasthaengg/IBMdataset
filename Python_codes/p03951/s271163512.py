n = int(input())
s = input()
t = input()

if len(s)+len(t)<= n:
  print(n)
  exit()
  
dup = min(len(s)+ len(t)-n, len(s), len(t))
for i in range(dup, 0 , -1):
  if s[-i:] == t[:i]:
    print(len(t)+len(s) - i)
    break
else:
  print(len(s)+len(t))