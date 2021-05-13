a,b,c= map(int, input().split())
pos = b//a
print(pos if pos<= c else c)