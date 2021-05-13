n = int(input())
a_l = list(map(int,input().split()))
b_l = list(map(int,input().split()))
c_l = list(map(int,input().split()))

ans = 0
before = None
for i in a_l:
    ans += b_l[i-1]
    if before == i-1:
        ans += c_l[before-1]
    before = i
print(ans)