n = int(input())
a_list = list(map(int, input().split()))
b_list =list(map(int, input().split()))
ans = 0
for i in range(n-1,-1,-1):
    if a_list[i+1] >= b_list[i]:
        a_list[i+1] -=b_list[i]
        ans += b_list[i]
    elif a_list[i+1] < b_list[i]:
        ans += a_list[i+1]
        ans += min(a_list[i], (b_list[i]-a_list[i+1]))
        a_list[i] = max(0,a_list[i] -(b_list[i]-a_list[i+1]))
        a_list[i+1]=0

    #print(a_list)
print(ans)