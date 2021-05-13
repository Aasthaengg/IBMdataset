# 28
N = int(input())
An = list(map(int, input().split(' ')))

ans = -1
flag = 0
while True:
    ans += 1
    for i in An:
        if i % 2 != 0: 
            flag = 1
            break
        An[An.index(i)] /= 2
    if flag != 0: break

print(ans)