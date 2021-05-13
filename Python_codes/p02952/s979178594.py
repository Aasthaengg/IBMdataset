n = int(input())
cnt = 0
for x in range(1,n+1):
    n_str = str(x)
    if len(n_str) % 2 != 0:
        cnt += 1
    
print(cnt)