N, A, B = map(int, input().split())

ans = 0

for n in range(1, N+1):
    digit_sum = sum([int(s) for s in str(n)])
    
    if A <= digit_sum <= B:
        ans += n
        
print(ans)