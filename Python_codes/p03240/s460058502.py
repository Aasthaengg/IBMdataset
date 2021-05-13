N = int(input())
info =[]
for n in range(N):
    info.append(list(map(int,input().split())))

def chech(Cx,Cy,x,y,h):
    if h > 0:
        H = h + abs(x-Cx) + abs(y-Cy)
        c_list.append(H)
    return 
    
for Cx in range(101):
    for Cy in range(101):
        c_list=[]
        c_list_zero=[]
        for i in info:
            x,y,h=i
            c_=chech(Cx,Cy,x,y,h)

        if len(set(c_list))==1:
            check_zero=True
            for i in info:
                x,y,h=i
                H = c_list[0]
                h_=max(H - (abs(x-Cx) + abs(y-Cy)),0)
                if h_ != h:
                    check_zero=False
                
            if check_zero==True:
                print(Cx,Cy,c_list[0])