N,A,B=map(int,input().split())
X=[int(x) for x in input().split()]
X.sort(reverse=True)
ave=sum(X[:A])/A
p=X[A-1]
c=0
o=0
for i in range(N):
  if X[i]==p:
    c +=1
  elif X[i]>p:
    o +=1
    

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
 
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
 
    return result
answer=0
if not o==0:
  answer=cmb(c,A-o)
else:
  for i in range(A,min(c,B)+1):
    answer += cmb(c,i)
print(ave)
print(answer)