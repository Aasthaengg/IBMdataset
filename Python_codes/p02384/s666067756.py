
class Dice:
    def __init__(self, label):
        self.d = label

    def roll(self, direction):
        if direction == "N":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[1], self.d[5], self.d[4], self.d[0]
        elif direction == "S":
            self.d[0], self.d[1], self.d[5], self.d[4] = self.d[4], self.d[0], self.d[1], self.d[5]
        elif direction == "E":
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[3], self.d[0], self.d[2], self.d[5]
        elif direction == "W":
            self.d[0], self.d[2], self.d[5], self.d[3] = self.d[2], self.d[5], self.d[3], self.d[0]
        else:
            pass

label = [int(i) for i in input().split()]
q = int(input())

dice1 = Dice(label)

for i in range(q):
    top, front = map(int, input().split())

    # ??¨????????¶???(4 * 6)???????????????????????¢??????
    cmd = "N" * 4 + ("W" + "N" * 4) * 3 + "NE" + "N" * 4 + "EE" + "N" * 4 

    for i in cmd:
        dice1.roll(i)

        if dice1.d[1] == front and dice1.d[0] == top:
            print(dice1.d[2])
            break