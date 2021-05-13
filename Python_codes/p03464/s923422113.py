K = int(input())
A = [int(x) for x in input().split()]
nmin = 2
nmax = 2
last = 1
for a in A[::-1]:
    nmin = ((nmin-1)//a+1)*a
    if(nmin>nmax):
        print(-1)
        break
    nmax = (nmax//a)*a+a-1
    last = a


else:
    print(nmin,nmax)
