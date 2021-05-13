a, b, c = list(map(int, input().split()))

d = a/b 

if d != int(d):
    d = int(d)+1 

print(int(d*c))