N = int(input())

cnt = 0
for i in range(1, N+1):
    i = str(i)
    if len(i)%2 != 0:
        cnt += 1
    
print(cnt)