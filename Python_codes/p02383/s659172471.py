class Dice:
    def __init__(self, num_list):
        self.vertical_faces = [num_list[0], num_list[1], num_list[5], num_list[4]]
        self.horizonal_faces = [num_list[0], num_list[3], num_list[5], num_list[2]]

    def roll(self, direction):
        if direction == 'N':
            self.vertical_faces = self.vertical_faces[1:] + self.vertical_faces[:1]
            self.horizonal_faces[0] = self.vertical_faces[0]
            self.horizonal_faces[2] = self.vertical_faces[2]
        elif direction == 'S':
            self.vertical_faces = self.vertical_faces[3:] + self.vertical_faces[:3]
            self.horizonal_faces[0] = self.vertical_faces[0]
            self.horizonal_faces[2] = self.vertical_faces[2]
        elif direction == 'E':
            self.horizonal_faces = self.horizonal_faces[1:] + self.horizonal_faces[:1]
            self.vertical_faces[0] = self.horizonal_faces[0]
            self.vertical_faces[2] = self.horizonal_faces[2]
        else:
            self.horizonal_faces = self.horizonal_faces[3:] + self.horizonal_faces[:3]
            self.vertical_faces[0] = self.horizonal_faces[0]
            self.vertical_faces[2] = self.horizonal_faces[2]

num_list = list(map(int, input().split()))

dice = Dice(num_list)

directions = input()

for i in directions:
    dice.roll(i)

print(dice.vertical_faces[0])