n = int(input())
food = [[int(i) for i in input().split()] for _ in range(n)]
food.sort(key=lambda x:sum(x),reverse=True)
hpns = [0,0]
for i in range(n): hpns[i%2] += food[i][i%2]
print(hpns[0]-hpns[1])