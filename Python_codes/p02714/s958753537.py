n = int(input())
s = input()

count = {"R":0,"G":0,"B":0}
for c in s:
  count[c] += 1

r,g,b = count.values()
ans = r*g*b
for i in range(1,(n-1)//2+1):
  for rgb in zip(s,s[i:],s[i*2:]):
    if len(set(rgb)) == 3:
      ans -=1
print(ans)