n=int(input())
A=list(map(int,input().split()))
ki=0  ;gu=0
for i in A:
    if i%2==1:
        ki+=1
    else:
        gu+=1
gu+=ki//2
ki%=2
if gu>=1 and ki==1:
    print("NO");exit()
print("YES")