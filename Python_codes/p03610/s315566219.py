s=input()
a=""
n=len(s)
for i in range(n//2):
  a+=s[i*2]
if n%2:
  a+=s[n-1]
print(a)