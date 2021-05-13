n = int(input())
p = [int(input()) for i in range(n)]

max_ = max(p)
flag = True
cnt = 0
for i in p:
    if i == max_ and flag:
        cnt += i // 2
        flag = False
    else:
        cnt += i
print(cnt)