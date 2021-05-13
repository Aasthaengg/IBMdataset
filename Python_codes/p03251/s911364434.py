n,m,x,y=map(int,input().split())
X= list(map(int,input().split()))
Y= list(map(int,input().split()))
maxx = max(X)
miny = min(Y)
frag = 0
for i in range(x+1,y+1):
    if i >maxx and i <=miny :
        frag = 1
        break
if frag == 1:
    print("No War")
else:
    print("War")