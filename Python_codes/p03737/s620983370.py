S=list(input().split())
ans=""
for i in range(3):
    ans+=chr(ord(S[i][0])-32)
print(ans)