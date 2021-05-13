i = list(map(int, input().split()))
print(["No", "Yes"][(i[0] + i[1]) >= i[2]])