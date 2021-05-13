def sol(lis):
    if len(lis)<=2:
        return abs(lis[0]-lis[1])
    costs = [0,abs(lis[0]-lis[1])]
    for i in range(2,len(lis)):
        x = abs(lis[i]-lis[i-1])
        y = abs(lis[i]-lis[i-2])
        costs.append(min(x+costs[-1],y+costs[-2]))
    return costs[-1]
input()
lis = list(map(int,input().split(' ')))
print(sol(lis))