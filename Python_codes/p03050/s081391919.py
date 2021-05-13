N = int(input())
cnt = 0
if N>2:
    for x in range(2,int(N**0.5)+1):
        if N%x==0:
            y = N//x
            if N//(x-1)==N%(x-1):
                cnt += x-1
            if N//(y-1)==N%(y-1):
                cnt += y-1
    cnt += N-1
print(cnt)