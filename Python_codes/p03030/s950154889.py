N=int(input())
restaurants = []
for i in range(N):
    S,P = input().split()
    P = int(P)
    restaurants.append([i+1,S, P])

restaurants.sort(key=lambda x: (x[1], -x[2]))

for r in restaurants:
    print(r[0])