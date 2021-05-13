# input
N, T = map(int, input().split())
rhr = []
r_append = rhr.append
for i in range(1, N + 1):
    c, t = map(int, input().split())
    r_append(
        {
            "index": i,
            "cost": c,
            "time": t
        }
    )

target_routes = [
    r
    for r in rhr
    if r["time"] <= T
]

if not target_routes:
    print("TLE")
else:
    target_routes.sort(key=lambda x: x["cost"])
    print(target_routes[0]["cost"])