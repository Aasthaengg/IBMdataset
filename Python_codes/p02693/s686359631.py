K = int(input())
A, B = map(int, input().split())
cnt = 0

for i in range(A, B+1):
    if i%K == 0:
        cnt += 1

if cnt >= 1:
    print("OK")
else:
    print("NG")    
