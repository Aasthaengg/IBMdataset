import sys
import math

n = int(sys.stdin.readline())


def koch(st, en):

    st_x, st_y = st[0], st[1]
    en_x, en_y = en[0], en[1]

    p1_x, p1_y = (2 * st_x + en_x) / 3, (2 * st_y + en_y) / 3
    p2_x, p2_y = (st_x + 2 * en_x) / 3, (st_y + 2 * en_y) / 3

    vec_x, vec_y = (p2_x - p1_x, p2_y - p1_y)  # vec p1->p2

    # 60°回転
    vec_r_x = vec_x * math.cos(math.pi / 3) - vec_y * math.sin(math.pi / 3)
    vec_r_y = vec_x * math.sin(math.pi / 3) + vec_y * math.cos(math.pi / 3)

    p3_x = vec_r_x + p1_x
    p3_y = vec_r_y + p1_y

    return (p1_x, p1_y), (p3_x, p3_y), (p2_x, p2_y)


def koch_r(n, st, en):
    if n == 0:
        return
    
    s, u, t = koch(st, en)
    
    koch_r(n - 1, st, s)
    print(f"{s[0]:f} {s[1]:f}")
    koch_r(n - 1, s, u)
    print(f"{u[0]:f} {u[1]:f}")
    koch_r(n - 1, u, t)
    print(f"{t[0]:f} {t[1]:f}")
    koch_r(n - 1, t, en)


st, en = (0, 0), (100, 0)

print(f"{st[0]:f} {st[1]:f}")
koch_r(n, st, en)
print(f"{en[0]:f} {en[1]:f}")

