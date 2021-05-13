A,B,T = map(int, input().split())
t = A
b = 0
while(t<=(T+0.5)):
    b += B
    t += A

print(b)
