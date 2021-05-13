x,y=map(int,input().split())
print(1000000 if (x,y)==(1,1) else (max(4-x,0)+max(4-y,0))*100000)