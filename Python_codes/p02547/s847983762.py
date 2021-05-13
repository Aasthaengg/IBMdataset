N = int(input())
A = 0
ans = "No"
for i in range(N):
    d1,d2 = map(int,input().split())
    if d1 == d2:
        A += 1
    else:
        A = 0
    if A >= 3:
        ans = "Yes"
print(ans)
