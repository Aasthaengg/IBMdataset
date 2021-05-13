a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if w>=v:
    print("NO")
    exit(0)
s=abs(b-a)/(v-w)
if s<=t:
    print("YES")
else:
    print("NO")