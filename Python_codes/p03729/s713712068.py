a,b,c = map(str,input().split())
ans = 'YES'
if a[-1] != b[0]:
    ans = 'NO'
if b[-1] != c[0]:
    ans = 'NO'
print(ans)