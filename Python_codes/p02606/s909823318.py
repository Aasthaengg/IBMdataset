lower, upper, d_baisuu = map(int, input().split())
 
cnt = 0
 
for num in range(lower, upper + 1):
    if (num % d_baisuu == 0):
        cnt += 1
 
print(cnt)