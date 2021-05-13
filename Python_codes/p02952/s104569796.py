N = int(input())
cnt =0
for i in range(1,N+1):
    if 1 <= i and i <= 9:
        cnt += 1
    
    if 100 <= i and i <= 999:
        cnt += 1

    if 10000 <= i and i <= 99999:
        cnt += 1

print(cnt)