input()

n = input()

ans = 0

for i in n:
    if i == "R":
        ans+=1
    else:
        ans-=1

if ans>0:
    print("Yes")
else:
    print("No")