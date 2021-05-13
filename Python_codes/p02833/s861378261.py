N = int(input())
if N & 1:
    print(0)
    exit()
    
N //= 2
cnt = 0
while N:
    cnt += N//5
    N //= 5
print(cnt)