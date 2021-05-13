mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    n = int(raw_input())
    
    arr = map(int,raw_input().split())
    
    ans = 0
    
    max_ele = max(arr)
    
    arr.sort()
    
    marked = [False] * (max_ele+5)
    
    for i in range(n):
        diff_prev = i-1 < 0 or arr[i] != arr[i-1]
        diff_next = i+1 >= n or arr[i] != arr[i+1]
        num = arr[i]
        if not marked[num]:
            cur = num 
            if diff_next and diff_prev:
                ans += 1
            while cur <= max_ele:
                marked[cur] = True
                cur += num
    
    print(ans)
    

main()