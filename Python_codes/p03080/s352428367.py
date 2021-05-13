N=int(input())

s=input()

Rcount=0
for i in range(N):
  if s[i]=='R':
    Rcount +=1
#print(Rcount)
print('Yes' if Rcount>N-Rcount else 'No')
