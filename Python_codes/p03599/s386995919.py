A, B, C, D, E, F = [int(_) for _ in input().split()]


def main(A, B, C, D, E, F):
    conc = -1
    ans = (1, 2)
    for na in range(F // (100 * A) + 1):
        for nb in range(F // (100 * B) + 1):
            if na == nb == 0:
                continue
            G = F - na * 100 * A - nb * 100 * B
            for nc in range(G // C + 1):
                for nd in range(G // D + 1):
                    W = na * 100 * A + nb * 100 * B + nc * C + nd * D
                    if 0 < W <= F and nc * C + nd * D <= E * (na * A + nb * B):
                        conc2 = 100 * (nc * C + nd * D) / W
                        if conc < conc2 <= 100 * E / (100 + E):
                            ans = (W, nc * C + nd * D)
                            conc = conc2
    return ans


print(*main(A, B, C, D, E, F))
