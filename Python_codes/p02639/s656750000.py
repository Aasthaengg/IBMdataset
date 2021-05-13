def inp():
    return int(input())
def inpL():
    return list(map(int,input().split()))

x = inpL()
for i in range(len(x)):
    if x[i] == 0:
        print(i+1)
        break