n,m,x,y=map(int,input().split())
listx=list(map(int,input().split()))
listy=list(map(int,input().split()))
if max(listx)>=y:
    print("War")
elif min(listy)<=x:
    print("War")
elif max(listx)>=min(listy):
    print("War")
else:
    print("No War")
