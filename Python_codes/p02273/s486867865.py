from collections import deque
if __name__ == "__main__":
    new_lines = deque([[[0.0, 0.0], [100.0, 0.0]]])
    n = int(input())
    sin60 = 3**0.5/2.0
    cos60 = 1.0/2.0
    for _ in range(n):
        lines = new_lines
        new_lines = deque()
        while lines:
            t1, t2 = lines.popleft()
            n1 = [(2.0*t1[0]+t2[0])/3.0, (2.0*t1[1]+t2[1])/3.0]
            n3 = [(t1[0]+2.0*t2[0])/3.0, (t1[1]+2.0*t2[1])/3.0]
            x, y = [n3[0]-n1[0], n3[1]-n1[1]]
            x60, y60 = [cos60*x - sin60*y ,sin60*x + cos60*y]
            n2 = [n1[0]+x60, n1[1]+y60]
            new_lines.append([t1, n1])
            new_lines.append([n1, n2])
            new_lines.append([n2, n3])
            new_lines.append([n3, t2])
    coordinates = list(zip(*new_lines))[0] + ([100.0, 0.0],)
    for coordinate in coordinates:
        print(*coordinate)
