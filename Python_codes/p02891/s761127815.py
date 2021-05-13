s = list(input())
k = int(input())

s2 = s + s
s3 = s + s + s

tmp = s[0]
c = 0
for i in range(1,len(s)):
    if s[i] == tmp:
        s[i] = "@"
        c += 1
    tmp = s[i] 

tmp = s2[0]
c2 = 0
for i in range(1,len(s2)):
    if s2[i] == tmp:
        s2[i] ="@"
        c2 += 1
    tmp = s2[i]

tmp = s3[0]
c3 = 0
for i in range(1,len(s3)):
    if s3[i] == tmp:
        s3[i] ="@"
        c3 += 1
    tmp = s3[i]

if c2-c == c3-c2:
    ans = c + (k-1)*(c2-c)
else:
    if k%2 != 0:
        ans = c + ((k-1)//2)*(c3-c)
    else:
        ans = c + ((k-2)//2)*(c3-c2) + c2 - c
print(ans)
