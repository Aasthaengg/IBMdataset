ABC = list(map(int, input().split()))

ABC.sort()
for i in ABC:
    if i % 2 == 0:
        print(0)
        break
else:
    print(ABC[0] * ABC[1])

