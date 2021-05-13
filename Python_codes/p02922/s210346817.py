A, B = map(int, input().split())

if B == 1:
    print(0)
    exit()

ans = A
for i in range(1000):
    if ans >= B:
        break
    else:
        ans += A-1
        
print(i+1)