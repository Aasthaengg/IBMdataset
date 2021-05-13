n = int(input())

a = []
for i in range(n):
    name, t = map(str, input().split())
    a.append([name, int(t)])

s = input()

cnt = 0
cnt_flag = 0
for i, j in a:
    if cnt_flag:
        cnt += j
    if s == i:
        cnt_flag = 1
print(cnt)
