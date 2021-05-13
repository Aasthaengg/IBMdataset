n = int(input())
lis = []
for _ in range(n):
    inp = list(map(int, input().split()))
    lis.append(inp)
lis.sort(key = lambda x:x[1])
time = 0
for i in range(len(lis)):
    time += lis[i][0]
    if time > lis[i][1]:
        print("No")
        exit()
print("Yes")