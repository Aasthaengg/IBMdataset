al=[chr(ord('a') + i) for i in range(26)]
reval=al[::-1]
s=list(input())
for si in s:
    al.remove(si)

if s==reval:
    print(-1)
elif len(al)!=0:
    print(''.join(s)+al[0])
else:
    k=0
    for i in range(26):
        if ord(s[25-i])>ord(s[24-i]):
            k=i
            break
    al=[chr(ord('a') + i) for i in range(26)]
    for i in range(24-k):
        al.remove(s[i])
    x=''
    for j in al:
        if j>s[24-k]:
            x=j
            break
    print(''.join(s[:24-k])+x)
