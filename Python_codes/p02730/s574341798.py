s=str(input())
n=len(s)
x=s[:(n-1)//2]
y=s[(n+3)//2-1:]
ans=0

for i in range(3):
    if s==s[::-1]:
        ans +=1

    if i==0:
        s=x
    elif i==1:
        s=y

print("Yes" if ans==3 else "No")