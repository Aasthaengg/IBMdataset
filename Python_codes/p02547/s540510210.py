n = int(input())
str_list = [list(input().split()) for _ in range(n)]
ans = 0
for i in range(n-2):
    if str_list[i][0] == str_list[i][1]:
        if str_list[i+1][0] == str_list[i+1][1]:
            if str_list[i+2][0] == str_list[i+2][1]:
                ans += 1
    
if ans:
    print('Yes')
else:
    print('No')
