a,b,k = map(int,input().split())
c = min(a,b)
list = []

for ci in range(1,c+1):
    if a % ci == 0 and b % ci == 0:
        list.append(ci)
print(list[-k])