a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
result='Yay!'
q=[a,b,c,d,e]
for i in q:
    for x in q:
        if i-x>k:
            result=':('
print(result)