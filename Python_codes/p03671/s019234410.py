bells = list(map(int, input().split()))

del bells[bells.index(max(bells))]

print(sum(bells))