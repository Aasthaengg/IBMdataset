a,b,c,d = map(int,input().split())
ans = 'No'
if -d <= a-c <= d:
    ans = 'Yes'
if -d <= a-b <= d:
    if -d <= b-c <= d:
        ans = 'Yes'
print(ans)