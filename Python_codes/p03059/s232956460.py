A, B, T = map(int, input().split())

time_count = 0
biscuit_count = 0
for i in range(1, 100):
    time_count += A
    if time_count > T + 0.5:
        break
    biscuit_count += B

print(biscuit_count)
    
