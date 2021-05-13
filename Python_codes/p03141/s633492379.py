N = int(input())
foods = []
for i in range(N):
    food = list(map(int,input().split()))
    foods.append(food)
foods.sort(key=lambda x: -(x[0]+x[1]))
#print(foods)
ans = 0
for i in range(N):
    if i%2 == 0:
        ans += foods[i][i%2]
    else:
        ans -= foods[i][i%2]
print(ans)