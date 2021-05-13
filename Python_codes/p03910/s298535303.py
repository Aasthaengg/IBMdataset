n = int(input())

ans = []
cnt = 0

for i in range(1, n+1):
    if cnt + i == n:
        ans.append(i)
        break
    elif cnt + i < n:
        cnt += i
        ans.append(i)
    else:
        dif = n - cnt
        ans[-dif] += dif
        break

for a in ans:
    print(a)