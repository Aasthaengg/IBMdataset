a, b = map(int, input().split())
if ((a + b) / 2) % 1 == 0:
    
    print(int((a + b) / 2))
else:
    print(int((a + b) / 2) + 1)