s = input()
n = len(s)
rs = sorted(s)
cnt = 0
ans = 'no'
for i in range(0, n-1):
    if rs[i] != rs[i+1]:
        cnt += 1
        if cnt == n-1:
            ans = 'yes'
            print(ans)
            exit()
print(ans)
