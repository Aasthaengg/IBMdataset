import math
N = int(input())
X = [0., 0.]
Y = [100., 0.]

rad = math.pi / 2 * 2 /3

def rot(rad, pos):
    return [math.cos(rad)*pos[0] - math.sin(rad)*pos[1], math.sin(rad)*pos[0] + math.cos(rad)*pos[1]]


def coh(left, right, cnt):
    
    if cnt == 0:
        return
    else:
        s = [(right[0] - left[0]) / 3 + left[0], (right[1] - left[1]) / 3 + left[1]]
        t = [(right[0] - left[0]) * 2 / 3 + left[0], (right[1] - left[1]) * 2 / 3 + left[1]]
        ux, uy = rot(rad, [t[0] - s[0], t[1] - s[1]])
        u = [ux + s[0], uy + s[1]]

        coh(left, s, cnt-1)
        print(*s)
        coh(s, u, cnt-1)
        print(*u)
        coh(u, t, cnt-1)
        print(*t)
        coh(t, right, cnt-1)

print(*X)
coh(X, Y, N)
print(*Y)
