N = int(input())

restaurants = []
for i in range(N):
    S, P = input().split()
    P = int(P)

    restaurants.append([S,-P, i+1])

restaurants.sort()

for x in restaurants:
    print(x[2])

