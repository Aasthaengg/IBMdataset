AB = [int(i) for i in input().split()]
if(AB[1] % AB[0] == 0):
    print(AB[0] + AB[1])
else:
    print(AB[1] - AB[0])