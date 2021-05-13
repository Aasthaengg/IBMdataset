table = [0] * 4*3*10

n = int(input())

for i in range(n):
    b,f,r,v = map(int, input().split())
    table[30*(b-1)+10*(f-1)+(r-1)] += v

for i in range(120):
    if i != 0 and i % 30 == 0:
        print("####################")
    print(" %d" % table[i], end="")
    if i%10 == 9:
        print()
