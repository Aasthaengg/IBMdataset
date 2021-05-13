N = int(input())
data = []
ans = []
for i in range(1, N+1):
  city, score = input().split()
  score = int(score)
  data.append([city, score, i])
city_list = [x[0] for x in data]
score_list = [x[1] for x in data]
num_list = [x[2] for x in data]
city_unique = sorted(set(city_list))

for city_u in city_unique:
  city_index = [i for i, x in enumerate(city_list) if x == city_u]
  for score in sorted([score_list[x] for x in city_index], reverse=True):
    print(num_list[score_list.index(score)])