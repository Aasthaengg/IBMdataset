s=input()
stack=0
x=0#消したペア数
for c in s:
    if c=='S':
        stack+=1
    else:
        if stack>0:
            stack-=1
            x+=1
print(len(s)-x*2)