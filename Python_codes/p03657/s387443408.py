#abc067 a 
a,b=map(int,input().split())
flag=False
x=[a,b,a+b]
for i in x:
    if i%3==0:
        flag=True
if flag:
 	print("Possible")
else:
 	print("Impossible")