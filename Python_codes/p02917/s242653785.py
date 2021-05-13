n = int(input())
B = list(map(int, input().split()))
cnt = 0
for i in range(len(B)):
    if i == 0:
       cnt += B[i]
    else:
        cnt += min(B[i-1], B[i])
        
cnt += B[len(B) - 1]
print(cnt)