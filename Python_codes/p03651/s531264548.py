n,k=map(int,input().split())
a=list(map(int,input().split()))
import fractions
a.sort()
#9,4,3>7
#9-(9-4-3)
#9 ;6 3 >5
if k in a:
    print("POSSIBLE")
    exit()

if k>a[-1]:
    print("IMPOSSIBLE")
    exit()

if a[0]==1:
    print("POSSIBLE")
    exit()

flag=0
gg = fractions.gcd(a[0], a[1])

for item in a[1:]:
    if item%gg!=0:
        flag=1

if flag==1:
    print("POSSIBLE")
    exit()
else:
    if k%gg==0:
        print("POSSIBLE")
        exit()
    else:
        print("IMPOSSIBLE")
        exit()


