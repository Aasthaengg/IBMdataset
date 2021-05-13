n = int(input())
a_li = list(map(int, input().split(" ")))
dif = 1000
ave = sum(a_li) / n
for i in range(n):
    if dif > abs(a_li[i] -ave):
        dif = abs(a_li[i] -ave)
        ans = i    
print(ans)