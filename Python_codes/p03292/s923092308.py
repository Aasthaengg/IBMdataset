a,b,c=map(int,input().split())
t=min(abs(b-a)+abs(c-b),abs(c-a)+abs(b-c),abs(b-c)+abs(a-b),abs(a-b)+abs(c-a),abs(a-c)+abs(b-a),abs(c-b)+abs(a-c))
print(t)