n = int(input())
s = str(input())
t = str(input())
val = s+t
for i in range(min(len(s),len(t))):
  if s[-1-i:] == t[:i+1]:
    val = s+t[i+1:]
 
print(len(val))