h,n = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
temp = 0
ans = "No"
for i in a:
    temp += i 
    if temp>=h:
        ans = "Yes"
        break
print(ans)