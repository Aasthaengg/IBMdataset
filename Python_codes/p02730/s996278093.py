s=input()
n=len(s)
s2=s[:(n-1)//2]
s3=s[(n+3)//2-1:]

count=0
for i in range(n//2):
    if s[i]==s[-(i+1)]:
        count+=1
for i in range((n-1)//2):
    if s2[i]==s2[-(i+1)]:
        count+=1
for i in range(n-(n+3)//2+1):
    if s3[i]==s3[-(i+1)]:
        count+=1

if count==n//2+(n-1)//2+n-(n+3)//2+1:
    print("Yes")
else:
    print("No")
