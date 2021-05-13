n = int(input())
h = list(map(int,input().split()))
sum_h = sum(h)
sum_now = 0
ans = 0

while sum_h != sum_now:
    for i in range(n):
        if h[i] != 0:
            start = i
            break
     
    goal = n
    
    for i in range(n-start):
        if h[start+i] == 0:
            goal = start + i
            break
            
        if start + i == n-1:
            goal == n
        
    water = min(h[start:goal])
    
    for i in range(start,goal):
        h[i] -= water
        
    ans += water
    sum_now += water * (goal-start)
        
print(ans)