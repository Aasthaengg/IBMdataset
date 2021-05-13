n =int(input())
s=input()

white =[0]
black=[0]

for i in range(n):
    white.append(white[i]+int(s[i]=='.'))
    black.append(black[i]+int(s[i]=='#'))

ans = 300000
for i in range(n+1):
    if ans>black[i]+white[n]-white[i]:
        ans=black[i]+white[n]-white[i]

print(ans)


