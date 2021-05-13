a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if a<b and v<=w:
    print("NO")
elif(w>v and (a>b or b>a or a==b)):
    print("NO")
else:
    if abs(b-a)<=t*abs(v-w):
        print("YES")
    else:
        print("NO")
