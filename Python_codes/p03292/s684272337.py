a,b,c=map(int,input().split())
print(abs(a-b)+abs(b-c)+abs(a-c)-max(abs(a-b),abs(b-c),abs(a-c)))