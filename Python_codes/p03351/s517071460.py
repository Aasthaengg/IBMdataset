a, b, c, d = map(int, input().split())

if a <= b <= c:
    if max(b - a, c - b) <= d:
        ans = 'Yes'
    else:
        ans = 'No'

elif c <= b <= a:
    if max(a - b, b - c) <= d:
        ans = 'Yes'
    else:
        ans = 'No'

else:
    if abs(c - a) <= d:
        ans = 'Yes'
    else:
        ans = 'No'
        
print(ans)