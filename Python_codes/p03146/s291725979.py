s = int(input())
n=[s]
for i in range(2,1000001):
    if s%2==0:
        s = s/2
    else:
        s = 3*s+1
    if s in n:
        print(i)
        break

    n.append(s)