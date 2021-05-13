a,b,c=map(int,input().split())
print(sum([abs(a-b), abs(b-c), abs(c-a)])-max([abs(a-b), abs(b-c), abs(c-a)]))