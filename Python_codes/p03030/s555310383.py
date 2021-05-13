N = int(input())
rank = []
for i in range(N):
  name, point = input().split(" ")
  rank.append({
    "name": name,
    "point": 100 - int(point),
    "id": i + 1
  })

rank.sort(key = lambda x: (x["name"], x["point"]))
print("\n".join(list(map(lambda r: str(r["id"]), rank))))