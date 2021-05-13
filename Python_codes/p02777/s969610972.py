n=2
s=[""]*n
a=[0]*n
s[:]=input().split()
a[:]=map(int,input().split())
u=input()
for ii in range(n):
  if s[ii]==u:
    a[ii]-=1
    break
print(" ".join([str(ii) for ii in a]))
