A, B = map(int, input().split())

for i in [A, B, A + B]:
    if i % 3 == 0:
        print("Possible")
        exit()
print("Impossible")
