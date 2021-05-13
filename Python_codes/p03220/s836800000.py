n=int(input())
t,a=map(int,input().split())
h=list(map(int,input().split()))

temp=[(abs((t-h[i]*0.006)-a),i+1) for i in range(n)]

print(min(temp)[1])