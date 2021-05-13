N = int(input())

restaurants = {}
for i in range(1, N+1):
    s, p = input().split()
    restaurants[i] = (s, int(p) * -1)

key = lambda x: (x[1][0], x[1][1])
restaurants_sorted = sorted(restaurants.items(), key=key)

for k in restaurants_sorted:
    print(k[0])