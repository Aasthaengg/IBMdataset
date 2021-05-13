n,q=list(map(int,input().split()))

n_t=[input().split() for i in range(n)]

p_time=0

while n_t:
    
    if int(n_t[0][1])<=q:
        p_time+=int(n_t[0][1])
        finish=n_t.pop(0)
        print(finish[0],p_time)
    else:
        
        n_t[0][1]=str(int(n_t[0][1])-q)
        n_t.append(n_t[0])
        p_time+=q
        del n_t[0]  