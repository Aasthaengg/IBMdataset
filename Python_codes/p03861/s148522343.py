def solve():
    a, b, x = map(int, input().split())
    
    if a != 0:
        return b//x - (a-1)//x
    else:
        return b//x + 1

print(solve())