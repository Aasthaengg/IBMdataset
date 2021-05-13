n=int(input())
lst=list(map(int,input().split()))
four=0
two=0
odd=0

for i in lst:
    if i%4==0:
        four+=1
    elif i%2==0:
        two+=1
    else:
        odd+=1

if four>=odd:
    print("Yes")
elif four+1==odd:
    if two==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")