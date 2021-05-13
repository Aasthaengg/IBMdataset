a,b,x = map(int, input().split())

# a,b,x = map(int, "9 9 2".split())
cnt=0

alfa = b//x + 1
beta = (a-1)//x + 1

print(alfa - beta)