s=input()
ans=1000
value=""
for i in range(len(s)-2):
    value=s[i:i+3]
    if abs(753-int(value))<=ans:
        ans=abs(753-int(value))
print(ans)