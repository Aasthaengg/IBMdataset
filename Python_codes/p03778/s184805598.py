w,a,b = map(int,input().split())

if a + w < b:
    ans = a + w -b
elif b + w < a:
    ans = b + w -a
elif a <b + w or b < a+w:
    ans = 0
print(abs(ans))