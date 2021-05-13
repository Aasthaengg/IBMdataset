N=int(input())

t_,x_,y_=(0,0,0)

ans = 'Yes'
for n in range(N):
    t,x,y = list(map(int,input().split()))
    T = t-t_
    manhattan_dist = abs(x-x_)+abs(y-y_)
#     print(T,manhattan_dist)
    if T >= manhattan_dist and manhattan_dist%2 == T%2:
        pass
    else:
        ans='No'
        
    t_,x_,y_ = t,x,y

print(ans)