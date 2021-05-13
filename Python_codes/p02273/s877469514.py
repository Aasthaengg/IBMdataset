import math

n = int(raw_input())

class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print self.x, self.y

def calcCoord(N, start, end):
    if N == 0:
        return [start]
    s = Coord((start.x * 2.0 + end.x) /3, (start.y * 2.0 + end.y) /3)
    t = Coord((start.x + end.x * 2.0) /3, (start.y + end.y * 2.0) /3)
    u = Coord(((t.x-s.x) - (t.y-s.y) * math.sqrt(3)) /2 + s.x, ((t.x-s.x) * math.sqrt(3) + (t.y-s.y)) /2 + s.y)
    if N == 1:
        return [start, s, u, t]
    return calcCoord(N-1, start, s) + calcCoord(N-1, s, u) + calcCoord(N-1, u, t) + calcCoord(N-1, t, end)
    
start = Coord(0.0, 0.0)
end = Coord(100.0, 0.0)
ans = calcCoord(n, start, end) + [end]
for i in range(len(ans)):
    print ans[i].x, ans[i].y