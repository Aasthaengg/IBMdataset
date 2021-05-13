N = int(input())
S = str(input())

l = list(S)
ans = l.count('R')*l.count('G')*l.count('B')
for i in range(N-2):
  a = l[i]
  for j in range(1, (N+1-i)//2):
    b, c = l[i+j], l[i+2*j]
    if (a!=b) and (b!=c) and (c!=a):
      ans -= 1
        
print(ans)
