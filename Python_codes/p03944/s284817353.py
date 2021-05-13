#数学的に解く
w,h,n = map(int,input().split())
cnt = 0
X = 0
Y = 0
while(cnt < n):
    x,y,a = map(int,input().split())
    
    if(a == 1):
        X = max(X,x)
    elif(a == 2):
        w = min(w,x)
    elif(a == 3):
        Y = max(Y,y)
    elif(a == 4):
        h = min(h,y)
    #print(w,h,X,Y)
    cnt += 1
print(max(w-X,0)*max(h-Y,0))