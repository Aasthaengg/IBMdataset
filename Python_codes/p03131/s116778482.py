k,a,b=map(int,input().split())
bis=1
coin=0
if b-a<=2:
    print(k+1)
else:
    print(((k-(a-1)-2)//2)*(b-a)+((k-(a-1)-2)%2)+b)