n=int(input())
def judge(t_1,x_1,y_1,t_2,x_2,y_2):
    dt=t_2-t_1 
    dx=abs(x_2-x_1) 
    dy=abs(y_2-y_1) 
    if dx+dy>dt:
        return True 
    else: 
        if (dt-dx-dy)%2 == 0:
            return False 
        else: 
            return True 
        
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
    
t_1,x_1,y_1=0,0,0 
for i in range(n):
    t_2,x_2,y_2=data[i]
    if judge(t_1,x_1,y_1,t_2,x_2,y_2): 
        print("No") 
        break 
    t_1,x_1,y_1=t_2,x_2,y_2 
else: 
    print("Yes")