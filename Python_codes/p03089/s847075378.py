N = int(input())
b = list(map(int,input().split()))
c =[]
while b:
    a = 0
    for i in range(len(b)-1,-1,-1):
        if i+1 == b[i]:
            a = b.pop(i)
            c.append(a)
            break
    if a == 0:
        print(-1)
        exit()
for i in range(len(c)-1,-1,-1):
    print(c[i])
