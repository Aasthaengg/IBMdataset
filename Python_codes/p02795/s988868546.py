h = int(input())
w = int(input())
n = int(input())

ans = 0
i = 0
m = max(h,w)
while True:
    ans +=1
    i += m
    if i >= n:
        print(ans)
        break

