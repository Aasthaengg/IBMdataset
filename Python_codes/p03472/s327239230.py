import math
def resolve():
    N, H = list(map(int, input().split()))
    attacks = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        attacks.append((a, 0))
        attacks.append((b, 1))
    attacks = sorted(attacks)
    damage = 0
    cnt = 0
    while damage < H:
        dam, once = attacks.pop()
        damage += dam
        cnt += 1
        if not once:
            cnt += math.ceil((H - damage) / dam)
            break
    print(cnt)



if '__main__' == __name__:
    resolve()