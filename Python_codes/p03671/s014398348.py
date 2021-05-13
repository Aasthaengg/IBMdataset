a,b,c=map(int, input().split()) 
box = [a,b,c]
print(min(box)+sorted(box)[1])