N = int(input())

restaurants = {}
for i in range(1, N+1):
    s, p = input().split()
    restaurants[i] = (s, int(p))

key = lambda x: x[1]
restaurants_sorted = sorted(restaurants.items(), key=key)

city_restraurant = []
city = ""
for restaurant in restaurants_sorted:
    if not city:
        city = restaurant[1][0]
        city_restraurant.append((restaurant[0], restaurant[1][1]))
    elif city == restaurant[1][0]:
        city_restraurant.append((restaurant[0], restaurant[1][1]))
    else:
        city_restraurant.sort(key=lambda x: x[1], reverse=True)
        for c in city_restraurant:
            print(c[0])
        city_restraurant = [(restaurant[0], restaurant[1][1])]
        city = restaurant[1][0]
city_restraurant.sort(key=lambda x: x[1], reverse=True)
for c in city_restraurant:
    print(c[0])