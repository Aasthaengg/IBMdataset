S=input()
char=len(S)

count=0
if char%2==0:
    low=(char//2)-1
    high=char//2
else:
    low=char//2
    high=char//2

while low>=0:
    if S[low]!=S[high]:
        count+=1
    low-=1
    high+=1

print(count)
