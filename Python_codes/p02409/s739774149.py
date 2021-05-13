class OfficialHouse:
    def __init__(self):
        self.bill = [[[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]],
                     [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]]]


    def input_bfrv(self, b, f, r, v):
        self.bill[b-1][f-1][r-1] += v

    def result(self):
        for i in range(4):
            for j in range(3):
                print("", ' '.join(map(str, self.bill[i][j])))
            if i != 3:
                print("####################")

oh = OfficialHouse()

n = int(input())

for i in range(n):
   bfrv = input().split()
   b = int(bfrv[0])
   f = int(bfrv[1])
   r = int(bfrv[2])
   v = int(bfrv[3])

   oh.input_bfrv(b, f, r, v)

oh.result()