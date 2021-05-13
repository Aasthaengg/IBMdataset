n = int(input())
a_l = list(map(int, input().split()))
ans = float('inf')
for a in a_l:
    c = 0
    while a%2 == 0:
        a = a/2
        c += 1
    ans = min(ans,c)
print(ans)