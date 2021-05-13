A,B,T=map(int, input().split())

time=0
biscuits=0

while True:
    time+=A
    if time>T+0.5:
        break
    biscuits+=B
print(biscuits)