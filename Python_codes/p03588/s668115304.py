N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

print(max(lst)[0] + max(lst)[1])
