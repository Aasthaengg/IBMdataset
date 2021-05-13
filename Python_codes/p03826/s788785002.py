A,B,C,D = (int(x) for x in input().split())
area1 = A*B
area2 = C*D
if(area1 > area2):
    print(area1)
elif(area1 < area2):
    print(area2)
else:
    print(area1)
