def koch_divide(p,q):
    v = [q[0]-p[0], q[1]-p[1]]
    s = [p[0]+v[0]/3, p[1]+v[1]/3]
    t = [q[0]-v[0]/3, q[1]-v[1]/3]
    u = [p[0]+v[0]*0.5-v[1]*0.288675, p[1]+v[0]*0.288675+v[1]*0.5]
    return [s,u,t,q]

def koch_curve(previous):
    vertices = [previous[0]]
    for p,q in zip(previous[:-1], previous[1:]):
        vertices.extend(koch_divide(p,q))
    return vertices

if __name__=='__main__':
    p_q = [[0.0, 0.0], [100.0, 0.0]]
    n = int(input())
    for _ in range(n):
        p_q = koch_curve(p_q)
    for vertex in p_q:
        print(" ".join(['{:.8f}'.format(x) for x in vertex]))