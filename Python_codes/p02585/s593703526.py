N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

route = {}
point = {}

for idx, p in enumerate(P):
    route[idx+1] = p
    point[p] = C[p-1]

all_max = -float('inf')
for origin_start in range(1, N+1):
    visit = set()
    visit.add(origin_start)
    now_point = 0
    max_point = -float('inf')
    start = origin_start
    for k in range(K):
        now_point += point[start]
        max_point = max(max_point, now_point)
        start = route[start]
        if start in visit:
            roup_count = k + 1
            roup_point = now_point
            if now_point > 0:
              if K // roup_count >= 0:
                now_point = (K // roup_count) * roup_point
                start = origin_start
                for _ in range(K % roup_count):
                    now_point += point[start]
                    max_point = max(max_point, now_point)
                    start = route[start]

              if K // roup_count - 1 >= 0:
                now_point = (K // roup_count - 1) * roup_point
                start = origin_start
                for _ in range(roup_count):
                    now_point += point[start]
                    max_point = max(max_point, now_point)
                    start = route[start]
            break
        visit.add(start)

    all_max = max(max_point, all_max)
print(all_max)