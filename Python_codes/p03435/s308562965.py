c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

for b1 in range(101):
    for b2 in range(101):
        for b3 in range(101):
            if c1[0] - b1 == c1[1] - b2 == c1[2] - b3:
                if c2[0] - b1 == c2[1] - b2 == c2[2] - b3:
                    if c3[0] - b1 == c3[1] - b2 == c3[2] - b3:
                        print("Yes")
                        exit()
else:
    print("No")