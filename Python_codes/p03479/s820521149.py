x,y = map(int,input().split())
li = []
while True:
    li += [x]
    x *= 2
    if x>y:
        break
print(len(li))