s = input()
n = len(s) #length s
aa = ['.'] * (n + 1)

if s[0] == '<':
  aa[0] = 0
if s[-1] == '>':
  aa[-1] = 0

for i in range(n-1):
  if s[i] ==  '>' and s[i+1] == '<':
    aa[i+1] = 0 
  elif s[i] == '<' and s[i+1] == '>':
    aa[i+1] = n
    
z = [i for i,x in enumerate(aa) if x == 0]
m = [i for i, x in enumerate(aa) if x == n]


for i in range(len(z)-1):
  aa[m[i]] = max(m[i]-z[i], z[i+1]-m[i])
  aa[m[i]+1] = z[i+1]-m[i]-1
  for j in range(z[i]+1, m[i]):
    aa[j] = aa[j-1] +1
  for k in range(m[i]+2,z[i+1]):
    
    aa[k] = aa[k-1]-1
for i in range(z[-1], n+1):
  if aa[i] == '.':
    aa[i] = aa[i-1]+1
for i in range(z[0]):
  if aa[i] == '.':
    aa[i] = z[0] - i
    

print(sum(aa))
