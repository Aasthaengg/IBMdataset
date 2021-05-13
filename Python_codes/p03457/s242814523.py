N = int(input())

t,x,y = 0,0,0
for _ in range(1, N+1):
    tn,xn,yn = map(int, input().split())
    step = tn-t
    step_needed = abs(x-xn) + abs(y-yn)
    
    if step < step_needed or step%2 != step_needed%2:
        print("No")
        break
    t,x,y = tn,xn,yn
    
else:  
    print("Yes")