n  = int(input())
As =  list(map(int,input().split(" ")))
ans = 0
for i,a in enumerate(As):
    if As[a-1] == i + 1:
        ans += 1
print(ans//2)