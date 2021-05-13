n = int(input())
p = list(map(int, input().split())) + [0]
cnt = 0
j = False

for i in range(n):
    if p[i] == i + 1:
        cnt += 1
        if p[i + 1] == i + 2:
            if j == False:
                cnt -= 1
                j = True
            else:
                j = False
    else:
        j = False
print(cnt)