n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
cnt = 0

for i in a:
    if x > i:
        x -= i
        cnt += 1
    elif x == i:
        cnt += 1
        break
    else:
        break
else:
    cnt -= 1

print(cnt)
