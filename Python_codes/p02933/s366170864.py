a=float(input())
s=input()
s1=list(s)
length=len(s1)
for x in s1:
    if ord(x)<97 or ord(x)>122:
        s1.remove(x)
length2=len(s1)
if length==length2 and 1<=length<=10 and 2800<=a<5000:
    if a<3200:
        print('red')
    else:
        print(s)