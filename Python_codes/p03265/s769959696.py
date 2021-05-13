import numpy as np

def resolve():
    x1, y1, x2, y2 = map(int, input().split())
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])

    rot_matrix = np.array([[0, -1], [1, 0]])
    p3 = p2 + np.dot(rot_matrix, p2 - p1)
    p4 = p3 + np.dot(rot_matrix, p3 - p2)

    print(p3[0], p3[1], p4[0], p4[1])
    
resolve()