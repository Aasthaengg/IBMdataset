N = int(input())

for x in range(1, 3501):
    for y in range(1, 3501):
        if 4*x*y-N*(x+y) != 0:
            if N*x*y/(4*x*y-N*(x+y)) == int(N*x*y/(4*x*y-N*(x+y))) and int(N*x*y/(4*x*y-N*(x+y))) > 0:
                print(x, y, int(N*x*y/(4*x*y-N*(x+y))))
                break
    else:
        continue
    break
