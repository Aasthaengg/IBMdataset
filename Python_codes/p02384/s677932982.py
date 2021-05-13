#East[north][top] -> E
class Dice():
 East = [ [0,3,5,2,4,0]
		 ,[4,0,1,6,0,3]
		 ,[2,6,0,0,1,5]
		 ,[5,1,0,0,6,2]
		 ,[3,0,6,1,0,4]
		 ,[0,4,2,5,3,0]
		 ]
 def __init__(self,N):
  self.label = N
  self.top = 1
  self.north = 5
 def move(self,ori):
  #print(self.top,self.north,ori)
  if ori=='S':
   t = self.top
   self.top = self.north
   self.north = 7-t
  elif ori=='N':
   t = self.top
   self.top = 7-self.north
   self.north = t
  elif ori=='E':
   east = self.East[self.north-1][self.top-1]
   self.top = 7-east
  elif ori=='W':
   east = self.East[self.north-1][self.top-1]
   self.top = east
 def gettop(self):
  return( self.label[self.top-1] )
  

label = list(map(int, input().split() ))
D = Dice(label)
q = int(input())
for qi in range(q):
 t,s = list(map(int, input().split() ))
 t = D.label.index(t)
 s = D.label.index(s)
 n = 5-s
 e = D.East[n][t]
 print(label[e-1])

