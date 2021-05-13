N = int(input())
h = list(map(int,input().split()))
cnt = 0
for i in range(max(h)):
    bol = 0
    for j in h:
        if j > i:
            bol = 1
        else:
            cnt += 1 if bol == 1 else 0
            bol = 0
    if bol == 0:
        cnt -= 1
print(max(h)+cnt)