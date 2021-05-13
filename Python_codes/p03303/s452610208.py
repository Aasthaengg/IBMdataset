s=input()
w=int(input())
n=len(s)//w
b=[]
if len(s)%w==0:
    for i in range(n):
        b.append(s[i*w])
else:
    for i in range(n+1):
        b.append(s[i*w])
print(''.join(b))
