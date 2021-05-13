# B
x, y = map(int, input().split())

bool = False
for c in range(0, 101):
    for t in range(0, 101):
        if c + t == x and 2*t + 4*c == y:
            bool = True
            break
            
print('Yes' if bool else 'No')