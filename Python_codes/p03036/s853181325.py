r, d, x = map(int, input().split())
print(r*x-d)
for _ in range(9):
    x = r*x-d
    print(r*x-d)
    
