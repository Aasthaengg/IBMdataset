s = input()

s = list(s)

L = len(s)

l = len(s)//2

c = 0

for i in range(l):
  if s[i] != s[L-1-int(i)]:
    c += 1
    
print(c)