s=int(input())

def collatz(n):
    if n%2==0:
        n=n/2
    else: 
        n=3*n+1
    return int(n)

l=[s]
while s!=1:
    s=collatz(s)
    l.append(s)

if l[0]==1:
    print(4)
elif l[0]==2:
    print(4)
else:
    print(len(l)+1)