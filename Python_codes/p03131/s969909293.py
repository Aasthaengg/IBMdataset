k,a,b = map(int,input().split())
ans = -1

if b-a<3:
    ans = k+1
else:
    if k<a+1:
        ans = k+1
    else:
        ope = k-(a-1)
        ope_ab = ope//2
        ans = ope_ab*b - (ope_ab-1)*a + ope % 2
        ans = int(ans)

print(ans)