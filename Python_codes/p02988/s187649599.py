n = int(input())
p = list(map(int,input().split()))
ans = int()

for num in range(1,len(p)-1):
    p1 = p[num - 1]
    p2 = p[num]
    p3 = p[num + 1]
    
    p_list = [p1,p2,p3]
    p_list.sort()
    if p_list[1] == p2:
        ans += 1
print(ans)