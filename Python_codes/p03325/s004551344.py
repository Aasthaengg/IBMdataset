n = int(input())
a_list = map(int, input().split())

cnt = 0
for a in a_list:
    while a % 2 == 0:
        cnt += 1
        a = a//2
print(cnt)