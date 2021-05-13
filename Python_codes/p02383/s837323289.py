class Dice:
  def __init__(self, list = map(str, range(1, 7))):
    self.top = list[0]
    self.front = list[1]
    self.right = list[2]
    self.left = list[3]
    self.back = list[4]
    self.bottom = list[5]

  def print_all(self):
    print "top = " + self.top
    print "front = " + self.front
    print "right = " + self.right
    print "left = " + self.left
    print "back = " + self.back
    print "bottom = " + self.bottom

  def roll_N(self):
    temp = self.top
    self.top = self.front
    self.front = self.bottom
    self.bottom = self.back
    self.back = temp

  def roll_S(self):
    temp = self.top
    self.top = self.back
    self.back = self.bottom
    self.bottom = self.front
    self.front = temp

  def roll_W(self):
    temp = self.top
    self.top = self.right
    self.right = self.bottom
    self.bottom = self.left
    self.left = temp

  def roll_E(self):
    temp = self.top
    self.top = self.left
    self.left = self.bottom
    self.bottom = self.right
    self.right = temp

my_dice = Dice(raw_input().split(" "))
order = raw_input()
for i in xrange(len(order)):
  if order[i] == "E":
    my_dice.roll_E()
  elif order[i] == "N":
    my_dice.roll_N()
  elif order[i] == "S":
    my_dice.roll_S()
  elif order[i] == "W":
    my_dice.roll_W()
  else:
    continue

print my_dice.top