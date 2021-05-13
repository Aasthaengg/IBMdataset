mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    n = int(raw_input())
    
    arr = [int(x) for x in raw_input().split()]
    
    s = set(arr)
    
    if len(s) == len(arr):
        print('YES')
    else:
        print('NO')
    

main()