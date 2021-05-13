n=input()
if len(n)%2==0:
    m=int(len(n)/2)
else:
    m=int((len(n)-1)/2)

a=0

for i in range(m):
    if n[i]==n[-1*(i+1)]:
       continue
    else:
        a+=1

if a==0:
    print('Yes')
else:
    print('No')
