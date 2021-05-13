X=int(input())
ans=0
for b in range(1,X+1):
    for p in range(2,X+2):
        if b**p<=X:
            if ans<b**p:
                ans=b**p
        else:
            break
print(ans)