n = int(input())
a_list = list(map(int,input().split()))
ans = 0
check = a_list[0]
for i in range(1,n):
    if check == a_list[i]:
        a_list[i] = 10001
        ans += 1
    check = a_list[i]
print(ans)