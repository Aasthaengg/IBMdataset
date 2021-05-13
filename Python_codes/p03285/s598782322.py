n=int(input())
can=True
for i in range(n//4+1):
    if (n-4*i)%7==0:
        print('Yes')
        can=False
        break
if can:
    print('No')