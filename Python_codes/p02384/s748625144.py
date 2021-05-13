class Dice:
  __table =[[0,1,2,3,4,5],[0,2,4,1,4,5],[0,4,3,2,1,5],[0,3,1,4,2,5],
            [1,5,2,3,0,4],[1,2,0,5,3,4],[1,0,3,2,5,4],[1,3,5,0,2,4],
            [2,5,4,1,0,3],[2,4,0,5,1,3],[2,0,1,4,5,3],[2,1,5,0,4,3],
            [3,5,1,4,0,2],[3,1,0,5,4,2],[3,0,4,1,5,2],[3,4,5,0,1,2],
            [4,2,5,0,3,1],[4,5,3,2,0,1],[4,3,0,5,2,1],[4,0,2,3,5,1],
            [5,1,3,2,4,0],[5,3,4,1,2,0],[5,4,2,3,1,0],[5,2,1,4,3,0]]
  __another = []
  def __init__(self,dice):
    self.dice = dice
    for t in self.__table:
      a = []
      for k,v in enumerate(t):
        a.append(dice[v])      
      self.__another.append(a)
      
  def output(self):
    print(self.dice[0])
    
  def right_dise(self,a,b):
    for t in self.__another:
      if t[0] == a and t[1] == b:
        return t[2]

  def move(self,str):
    if str == 'N':
      temp = self.dice[0]
      self.dice[0] = self.dice[1]
      self.dice[1] = self.dice[5]
      self.dice[5] = self.dice[4]
      self.dice[4] = temp
    elif str == 'S':
      temp = self.dice[0]
      self.dice[0] = self.dice[4]
      self.dice[4] = self.dice[5]
      self.dice[5] = self.dice[1]
      self.dice[1] = temp

    elif str == 'E':
      temp = self.dice[0]
      self.dice[0] = self.dice[3]
      self.dice[3] = self.dice[5]
      self.dice[5] = self.dice[2]
      self.dice[2] = temp
      
    elif str == 'W':
      temp = self.dice[0]
      self.dice[0] = self.dice[2]
      self.dice[2] = self.dice[5]
      self.dice[5] = self.dice[3]
      self.dice[3] = temp      
  
      
di = list(map(int,input().split()))
di = Dice(di)
num = int(input())

while num > 0:
  v1,v2 = map(int,input().split())
  re = di.right_dise(v1,v2)
  print(re)
  num -= 1
  
