n=int(input())
a=list(input().split())
if n > 3:
    ans=''
    ans += ' '.join(a[::-2])
    if n%2==0:
        ans += ' ' + ' '.join(a[0::2])
    else:
        ans += ' ' + ' '.join(a[1::2])
    print(ans)
else:
    ans=[]
    for i in range(n):
        ans.append(a[i])
        ans.reverse()
    print(' '.join(ans))