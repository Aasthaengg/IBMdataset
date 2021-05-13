a, b = map(int,input().split())
cnt = 0
for i in range(a, b+1):
    i_s = str(i)
    i_r = 0
    for j in range(len(i_s)):
        i_r *= 10
        i_r += int(i_s[-j-1])
    if i == i_r:
        cnt += 1
print(cnt)