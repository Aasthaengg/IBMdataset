n=int(input())
a=list(input())
b=list(input())
c=list(input())
co=0
for a,b,c in zip(a,b,c):
    if a==b==c:
        co+=0
    elif a==b or a==c or b==c:
        co+=1
    elif a!=b!=c:
        co+=2
print(co)