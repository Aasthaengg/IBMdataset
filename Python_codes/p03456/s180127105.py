a, b = input().split()
ab = int(str(a) + str(b))
print(["No", "Yes"][ab % (ab ** 0.5) == 0])