S=input()
a=0
b=0
c=0

for i in range(len(S)):
    if S[i]=="a":
        a+=1
    if S[i]=="b":
        b+=1
    if S[i]=="c":
        c+=1

if a==b and a==c or a==b and a==c+1 or a==b and a==c-1 or b==c and c==a+1 or b==c and b==a-1 or c==a and a==b+1 or c==a and a==b-1:
    print("YES")
else:
    print("NO")
