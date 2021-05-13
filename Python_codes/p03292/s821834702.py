a,b,c=map(int,input().split())
print(min(abs(a-b)+abs(b-c),abs(b-c)+abs(c-a),abs(c-a)+abs(a-b)))