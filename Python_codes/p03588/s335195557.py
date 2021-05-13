n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
lis.append([int(),0])
lis = sorted(lis, key=lambda x:x[0])

#print(lis)
lis.reverse()
#print(lis)
print(lis[0][0]+lis[0][1])