#  ABC 086 C - Traveling
N = int(input())

t = [0] * (N+1)
x = [0] * (N+1)
y = [0] * (N+1)

for i in range(1,N+1):
    t[i],x[i],y[i] = map(int,input().split())

boolian = True    
        
for i in range(N):
    delta_t = t[i+1] - t[i]
    delta_x = x[i+1] - x[i]
    delta_y = y[i+1] - y[i]
    
    delta_x = abs(delta_x)
    delta_y = abs(delta_y)
    
    delta_sum = delta_x + delta_y
    
    k = delta_sum % 2 
    j = delta_t % 2

    if -delta_t <= delta_sum and delta_sum <= delta_t:
        if k == 0 and j == 0:
            boolian = True
            continue
        if k == 1 and j == 1:
            boolian = True
            continue
        else:
            boolian = False
            print('No')
            break
    else:
        boolian = False
        print('No')
        break

if boolian == True:
    print('Yes')