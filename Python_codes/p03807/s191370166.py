n=int(input())
a=list(map(int,input().split()))

odd=0
even=0

for aa in a:
    if aa%2==0:
        even+=1
    else:
        odd+=1

#odd+odd=even
#even+even=even

#もし奇数がペアが作れない場合,NO
if odd%2==1 and ( odd>2 or even>0):
    print("NO")
else:
    print("YES")
