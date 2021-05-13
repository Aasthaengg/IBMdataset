n, k = map(int, input().split())
an = list(map(int, input().split()))
mini = min(an)
need = 0
for a in an:
    if a != mini:
        need += 1
print(-(-need//(k-1)))
