N = int(input())
cnt = 0
for a in range(1, 10**6+1):
    if (a * a) < N :
        cnt = cnt + 1
    else:
        break
    for b in range(a+1, 10**6+1):
        if a*b < N:
            cnt = cnt + 2
        else:
            break
print(cnt)