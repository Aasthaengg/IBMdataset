N, A, B = map(int, input().split())
 
ma = A + B * (N - 1)
mi = B + A * (N - 1)
 
if ma < mi:
    print(0)
elif ma==mi:
    print(1)
else:
    print(ma - mi + 1)