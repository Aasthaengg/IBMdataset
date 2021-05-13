def sol():
    import sys
    input=sys.stdin.readline
    h,w,n=map(int,input().split())
    d={}
    for i in range(n):
        y,x=map(int,input().split())
        if (y,x) in d:
            d[(y,x)]+=1
        else:
            d[(y,x)]=1
        if y+1<=h and (y+1,x) in d:
            d[(y+1,x)]+=1
        elif y+1<=h:
            d[(y+1,x)]=1
        if y+2<=h and (y+2,x) in d:
            d[(y+2,x)]+=1
        elif y+2<=h:
            d[(y+2,x)]=1
 
        if x+1<=w and (y,x+1) in d:
            d[(y,x+1)]+=1
        elif x+1<=w:
            d[(y,x+1)]=1
        if x+2<=w and (y,x+2) in d:
            d[(y,x+2)]+=1
        elif x+2<=w:
            d[(y,x+2)]=1
        if x+1<=w and y+1<=h and (y+1,x+1) in d:
            d[(y+1,x+1)]+=1
        elif x+1<=w and y+1<=h:
            d[(y+1,x+1)]=1
        if x+2<=w and y+1<=h and (y+1,x+2) in d:
            d[(y+1,x+2)]+=1
        elif x+2<=w and y+1<=h:
            d[(y+1,x+2)]=1
        if x+1<=w and y+2<=h and (y+2,x+1) in d:
            d[(y+2,x+1)]+=1
        elif x+1<=w and y+2<=h:
            d[(y+2,x+1)]=1
        if x+2<=w and y+2<=h and (y+2,x+2) in d:
            d[(y+2,x+2)]+=1
        elif x+2<=w and y+2<=h:
            d[(y+2,x+2)]=1
    ans=[0]*10
    for i in d:
        if i[0]>2 and i[1]>2:
            ans[d[i]]+=1
 
    ans[0]=h*w-sum(ans)-w*2-h*2+4
    for i in ans:
        print(i)
        
if __name__=="__main__":
    sol()