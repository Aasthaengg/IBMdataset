alpha=[chr(ord('a') + i) for i in range(26)]
a=list(input())
N=int(input())
for i in range(len(a)):
   s=26-alpha.index(a[i])
   if s<=N and s!=26:
      a[i]="a"
      N-=s
s=alpha.index(a[-1])
s=(s+N)%26
a[-1]=alpha[s]
print(*a,sep="")