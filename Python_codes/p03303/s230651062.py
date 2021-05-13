s=input()
w=int(input())
ans=""
if len(s)%w==0:
    x=len(s)//w
else:
    x=len(s)//w +1
for i in range(x):
    ans+=s[i*w]
print(ans)