# D - Harlequin / 
n=int(input())
a=[int(input()) for i in range(n)]
odd,even=0,0
for aa in a:
    if aa%2==1:
        odd+=1
    else:
        even+=1
if even==n:
    print('second')
else:
    print('first')
