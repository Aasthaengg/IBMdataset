N = int(input())
flag = 0
state = 0
dic = {}
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        state += 1
    else:
        state = 0
    if state >= 3:
        flag = 1

if flag:
    print("Yes")
else:
    print("No")