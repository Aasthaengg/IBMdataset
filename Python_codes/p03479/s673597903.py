x,y=input().split();
k,w=int(y)//int(x),1
while 2**(w-1)<=k:w=w+1
print(w-1)