n=int(input())
a=[]
for i in range(n):
    st,IN=map(str,input().split())
    a.append([st,IN])
a=a[::-1]
x=input()
ss=0
for y in a:
    if y[0]==x:
        break
    ss+=int(y[1])
print(ss)
