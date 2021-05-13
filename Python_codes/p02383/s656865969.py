class Dice:
  
  def __init__(self, input_dice):
    self.flow = [input_dice[3], input_dice[1], input_dice[0], input_dice[5], input_dice[2], input_dice[4]]
    self.dice = [i for i in range(6)]
  
  def setNumber(self, n0, n1, n2, n3, n4, n5):
    self.dice[0] = n0
    self.dice[1] = n1
    self.dice[2] = n2
    self.dice[3] = n3
    self.dice[4] = n4
    self.dice[5] = n5
    return self.dice
    
  def roll(self, dir):
    if dir == 'S':
      self.setNumber(self.flow[0], self.flow[2], self.flow[5], self.flow[1], self.flow[4], self.flow[3])
      self.flow = self.dice
      return self.dice
    if dir == 'N':
      self.setNumber(self.flow[0], self.flow[3], self.flow[1], self.flow[5], self.flow[4], self.flow[2])
      self.flow = self.dice
      return self.dice
    if dir == 'W':
      self.setNumber(self.flow[2], self.flow[1], self.flow[4], self.flow[0], self.flow[3], self.flow[5])
      self.flow = self.dice
      return self.dice
    if dir == 'E':
      self.setNumber(self.flow[3], self.flow[1], self.flow[0], self.flow[4], self.flow[2], self.flow[5])
      self.flow = self.dice
      return self.dice

dice = list(map(int, input().split()))
d = Dice(dice)
dir = list(input())
for i in range(len(dir)):
  d.roll(dir[i])
print(d.dice[2])
