N=int(input())
Ls = list(map(int,input().split()))
score=0
for i in range(0,N-2):
  a = Ls[i]
  for j in range(i+1, N-1):
      b = Ls[j]
      for k in range(j+1, N):
        c = Ls[k]
        if ((a+b>c)&(a+c>b)&(b+c>a)&(a!=b)&(a!=c)&(b!=c)):
          score+=1

print(score)