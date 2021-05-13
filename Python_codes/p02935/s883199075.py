n = int(input())
m = sorted(list(map(int,input().split())))
if len(m) == 2:
    print(sum(m) / 2)
    exit()

ans = (m[0] + m[1]) / 2
for i in range(2,n):
    ans = (ans + m[i]) / 2
    
print(ans)