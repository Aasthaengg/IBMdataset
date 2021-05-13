n = int(input())
l = list(map(int,input().split()))
sl = sum(l)
ans = 'Yes'
for i in l:
    if sl - i*2 <= 0:
        ans = 'No'
print(ans)