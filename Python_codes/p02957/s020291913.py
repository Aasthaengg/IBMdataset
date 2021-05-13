inp1,inp2=map(int, input().split())
value=inp1+inp2
if value%2==0:
    print(int(value/2))
else:
    print("IMPOSSIBLE")