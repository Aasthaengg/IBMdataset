s=input()
k=int(input())
ans=""
for i in s[:-1]:
    if i=="a":
        ans+=i
        continue
    if k>=123-ord(i):
        k-=123-ord(i)
        ans+="a"
    else:
        ans+=i
i=s[-1]
ans+=chr((ord(i)+k-97)%26+97)
print(ans)