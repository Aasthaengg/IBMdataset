A, B, C, D, E, F = map(int, input().split())

noudo = 0
satou = 0
sato_mizu = 100 * A

for x in range(F//(100*A)+1):
    for y in range(F//(100*B)+1):
        if 100 * (A*x+B*y) > F:
            break

        for z in range(F // C + 1):
            if C * z > (A * x + B * y) * E:
                break

            if 100 * (A * x + B * y) + C * z > F:
                break

            for w in range(F // C + 1):
                if (C*z + D*w + 100 * (A*x+B*y)) == 0:
                    break

                if C*z + D*w > (A * x + B * y)*E:
                    break

                if 100 * (A*x+B*y)+C*z + D*w > F:
                    break

                if noudo < 100* (C*z + D*w)/(C*z + D*w + 100 * (A*x+B*y)):
                    noudo = 100* (C*z + D*w)/(C*z + D*w + 100 * (A*x+B*y))
                    sato_mizu = (C*z + D*w + 100 * (A*x+B*y))
                    satou = C*z + D*w
print(sato_mizu, satou)