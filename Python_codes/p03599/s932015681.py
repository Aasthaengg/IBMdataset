A, B, C, D, E, F = map(int, input().split())

memo = {}
memo.update(density=0, sugerwater=0, suger=0)
for a in range(F//(100*A) + 1):
    for b in range(F//(100*B) + 1):
        for c in range(E*(A*a + B*b)//C + 1):
            for d in range(E*(A*a + B*b)//D + 1):
                # print(100*(A*a + B*b) + C*c + D*d)
                if 100 * (A * a + B * b) + C * c + D * d <= F and C * c + D * d <= E * (A * a + B * b) and (100 * (A * a + B * b) + C * c + D * d) != 0:
                    dens_tmp = 100*(C*c + D*d)/(100*(A*a + B*b) + C*c + D*d)
                    if dens_tmp >= memo['density']:
                        memo.update(density=dens_tmp, sugerwater=100 *
                                    (A * a + B * b) + C * c + D * d, suger=C * c + D * d)

print(memo['sugerwater'], memo['suger'])