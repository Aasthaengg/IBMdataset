n = int(input())
a_li = [[0]*2 for i in range(n)]
for i in range(n):
    a_li[i][1],a_li[i][0] = map(int,input().split())
a_li.sort()
time = 0
for i in range(n):
    time += a_li[i][1]
    if time > a_li[i][0]:
        print("No")
        exit()
print("Yes")