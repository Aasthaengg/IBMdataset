n = int(input())
val_list =list(map(int, input().split()))
val_list.sort()
ans = val_list[0]*0.5**(n-1)
for i in range(1,n):
    ans += val_list[i]*(1/2)**(n-i)
    
print(ans)