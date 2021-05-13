mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    #A, B = [int(x) for x in raw_input().split()]
    n = int(raw_input())
    
    arr = [int(x) for x in raw_input().split()]
    
    ans = [-1] * n
    
    total_xor = 0
    
    for num in arr:
        total_xor ^= num
    
    for i in range(n):
        ans[i] = total_xor ^ arr[i]
        ans[i] = str(ans[i])
    
    print(' '.join(ans))
    

main()