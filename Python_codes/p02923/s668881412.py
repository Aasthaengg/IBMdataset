n = int(input())
h_list= list(map(int, input().split()))
ans =0
result = 0
for i in range(n):

    if i == n-1:
        break
        
    
    if h_list[i] >=h_list[i+1]:
        ans += 1
    else:
        ans = 0
        continue
    result=max(result, ans)
    
print(result)