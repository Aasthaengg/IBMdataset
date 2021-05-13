class dice:
    def __init__(self, f):
        assert(len(f) == 6)
        self.face = f
        self.N = [1, 5, 2, 3, 0, 4]
        self.S = [4, 0, 2, 3, 5, 1]
        self.E = [3, 1, 0, 5, 4, 2]
        self.W = [2, 1, 5, 0, 4, 3]
        self.R = [0, 2, 4, 1, 3, 5]

    def rotate(self, dir):
        rot = self.__getattribute__(dir)
        old = self.face
        new = [-1 for _ in range(6)]
        for i in range(6):
            new[i] = old[rot[i]]
        self.face = new


F = list(map(int, input().split()))
D = dice(F)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    for _ in range(4):
        if a == D.face[0]:
            break
        else:
            D.rotate('N')
    if a != D.face[0]:
        for _ in range(4):
            if a == D.face[0]:
                break
            else:
                D.rotate('E')
    assert(a == D.face[0])
    for _ in range(4):
        if b == D.face[1]:
            break
        else:
            D.rotate('R')
    assert(b == D.face[1])
    print(D.face[2])
