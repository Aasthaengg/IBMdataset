import itertools

n = int(input())

x_list = []
y_list = []
cnt = 0
distance = 0

for i in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

for a in itertools.permutations(range(n)): #順列を生成して、それらに対して処理
    cnt += 1
    for i in range(len(a)-1):
        #　各順列に対する処理
        distance += ((x_list[a[i]]-x_list[a[i+1]])**(2) + (y_list[a[i]]-y_list[a[i+1]])**(2))**(1/2)
ans = distance/cnt
print(ans)