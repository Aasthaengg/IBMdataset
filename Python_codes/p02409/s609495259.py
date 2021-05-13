class OfficialHouse:
    def __init__(self):
        self.room = [[[0 for k in range(10)] for j in range(3)] for i in range(4)]
    def inout(self, b, f, r, v):
        self.room[b-1][f-1][r-1] += v
    def output(self):
        for i in range(4):
            for j in range(3):
                s = ""
                for k in range(10):
                    s += " %d" % (self.room[i][j][k])
                print s
            if i != 3:
                print "####################"

if __name__ == "__main__":
    oh = OfficialHouse()

    n = int(raw_input())
    for i in range(n):
        b, f, r, v = map(int, raw_input().split())
        oh.inout(b,f,r,v)
    oh.output()