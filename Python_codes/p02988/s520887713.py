n = int(input())
ans = 0
p_list = list(map(int,input().split()))
for i in range(0,n-2):
    a = p_list[i]
    b = p_list[i+1]
    c = p_list[i+2]
    if min(a,b,c) != b and max(a,b,c) != b:
        ans += 1
print(ans)