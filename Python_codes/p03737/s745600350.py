a=list(input().split())
ans=""
for i in a:
    ans+=chr(ord(i[0])-32)
print(ans)