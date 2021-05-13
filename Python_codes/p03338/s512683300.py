n = int(input())
s = list(input())
half = int(n/2)

max1 = 0
for i in range(half):
  f = set(s[:half-i])
  b = set(s[half-i:])
  union = len(f&b)
  if max1 < union:
    max1 = union
  #else:
    #break

max2 = 0
for i in range(half):
  f = set(s[:half+i])
  b = set(s[half+i:])
  union = len(f&b)
  if max2 < union:
    max2 = union
  #else:
    #break
    
ans = max1 if max1>max2 else max2
print(ans)