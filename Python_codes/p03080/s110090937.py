n=int(input())
r=0
b=0
s=list(input())

for i in range(n):
    if s[i]=="B":
        b+=1
    else:
        r+=1

if r>b:
    print("Yes")
else:
    print("No")