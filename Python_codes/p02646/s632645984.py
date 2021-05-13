a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
k=abs(b-a)
s=w-v

print("YES" if s<=0 and k+t*s<=0 else "NO")