str=list(input())
n=int(input())
for i in range(n):
    a=input().split()
    s=int(a[1]);f=int(a[2])+1
    str1=str[s:f]
    if a[0]=='replace':
        ar=list(a[3])
        str[s:f]=ar
    elif a[0]=='print':
        ans=''.join(str1)
        print(ans)
    else:
        str2=str1[::-1]
        str[s:f]=str2
