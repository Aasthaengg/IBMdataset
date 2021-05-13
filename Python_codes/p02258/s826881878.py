n = int(input())

# initial observation
cur_min = int(input())
max_diff = -1 * (10**9) - 1

for i in range(n - 1) :
    num = int(input())
    
    max_diff = max(max_diff, num - cur_min)
    
    if num < cur_min :
        cur_min = num
    
print(max_diff)
