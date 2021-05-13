N, K = [int(x) for x in input().split(" ")]
 
placed = 0
elm = []
for i in range(N):
  a, b = input().split(" ")
  elm.append({
    "order": i + 1,
    "element": int(a),
    "count": int(b)
  })

elm.sort(key=lambda e: (e["element"], e["order"]))
for i in range(len(elm)):
  e = elm[i]
  placed += e["count"]
  if placed >= K:
    print(e["element"])
    break