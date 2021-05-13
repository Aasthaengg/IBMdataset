n,m = map(int, input().split())
List = list(map(int, input().split()))
List.sort()
cand = []
for _ in range(m):
  b,c = map(int,input().split())
  cand.append((b,c))
bc = sorted(cand, key=lambda x: x[1], reverse=True)
i = 0
for b, c in bc:
    while b:
        if i < n and List[i] < c:
            List[i] = c
            b -= 1
        else:
            break
        i += 1
print(sum(List))