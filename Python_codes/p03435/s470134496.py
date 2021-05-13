c=[list(map(int,input().split())) for _ in range(3)]
for a0 in range(-100,201):
    for a1 in range(-100,201):
        for a2 in range(-100,201):
            if c[0][0]-a0==c[1][0]-a1==c[2][0]-a2:
                if c[0][1]-a0==c[1][1]-a1==c[2][1]-a2:
                    if c[0][2]-a0==c[1][2]-a1==c[2][2]-a2:
                        print("Yes")
                        exit()
print("No")