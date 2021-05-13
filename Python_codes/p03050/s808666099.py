N = int(input())
cnt = 0
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        q = N//i
        m = i-1
        if q<m:
            cnt += m
        m = N//i-1
        q = i
        if q<m:
            cnt += m
print(cnt)