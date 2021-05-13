n = int(input())
cnt = 0
for m in range(1,n+1,2):
    if len([i for i in range(1,m+1) if m%i==0])==8:
        cnt += 1
print(cnt)