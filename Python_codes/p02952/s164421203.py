n = int(input())
cnt = 0
for i in range(1,10**5+1):
    if (i <= n) and (len(str(i)) in [1,3,5]):
        cnt += 1
print(cnt)