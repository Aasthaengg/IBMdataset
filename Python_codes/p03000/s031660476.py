n, x = map(int, input().split())
l_l = map(int, input().split())
z = 0
cnt = 1
for i in l_l:
    z += i
    if z <= x:
        cnt += 1
    else:
        break
print(cnt)