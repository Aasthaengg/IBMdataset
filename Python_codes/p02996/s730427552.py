n = int(input())
AB = []
for i in range(n):
    a,b = map(int,input().split())
    AB.append([a,b])
AB.sort(key=lambda x: x[1])
sum = 0
for a,b in AB:
    sum += a
    if sum > b:
        print('No')
        exit()
print('Yes')