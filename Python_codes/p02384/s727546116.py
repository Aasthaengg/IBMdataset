from collections import deque

class Dice():
    # def __init__(self, sequence):
    #     self.v = deque([seq[5], seq[4], seq[0], seq[1]])
    #     self.h = deque([seq[3], seq[0], seq[2], seq[5]])

    def __init__(self, seq):
        self.v = deque([seq[5], seq[4], seq[0], seq[1]])
        self.h = deque([seq[3], seq[0], seq[2], seq[5]])

    def lotate(self, direction):

        if   direction == "E":
            self.h.rotate()
            self.v[2] = self.h[1]
            self.v[0] = self.h[3]

        elif direction == "W":
            self.h.rotate(-1)
            self.v[2] = self.h[1]
            self.v[0] = self.h[3]

        elif direction == "N":
            self.v.rotate(-1)
            self.h[1] = self.v[2]
            self.h[3] = self.v[0]

        elif direction == "S":
            self.v.rotate()
            self.h[1] = self.v[2]
            self.h[3] = self.v[0]

        else:
            pass

    def disp_top_face(self):
        return self.v[2]

    def disp_front_face(self):
        return self.v[3]

    def disp_back_face(self):
        return self.v[1]

    def disp_right_face(self):
        return self.h[2]

    def disp_left_face(self):
        return self.h[0]

    def disp_bottom_face(self):
        return self.h[3]

if __name__ == "__main__":

    param = input().split(" ")

    seq = [int(a) for a in param]
    d = Dice(seq)

    n = int(input())

    for _ in range(n):

        param = input().split()
        top = int(param[0])
        front = int(param[1])

        flag = 1

        while(flag):

            for _ in range(4):
                d.lotate("S")

                if d.disp_front_face() == front :
                    flag = 0
                    break

            if flag != 0:
                d.lotate("E")


        flag = 1

        while(flag):

            for _ in range(4):
                d.lotate("E")

                if d.disp_top_face() == top :
                    flag = 0
                    break

        print(d.disp_right_face())

