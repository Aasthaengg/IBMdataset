n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
d.sort()
t.sort()
i=0
j=0
stat=''
while i < n and j < m:
  if d[i]==t[j]:
    i+=1
    j+=1
  elif d[i]>t[j]:
    print('NO')
    exit()
  elif d[i]<t[j]:
    i+=1
print('YES' if j==m else 'NO')

