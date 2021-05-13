import sys

class Dice(object):
	def __init__(self, data):
		self.dice=data
	def roll_n(self):
		self.dice=(self.dice[1],self.dice[5],self.dice[2],
					self.dice[3],self.dice[0],self.dice[4])
	def roll_e(self):
		self.dice=(self.dice[3],self.dice[1],self.dice[0],
					self.dice[5],self.dice[4],self.dice[2])
	def roll_w(self):
		self.dice=(self.dice[2],self.dice[1],self.dice[5],
					self.dice[0],self.dice[4],self.dice[3])				
	def roll_s(self):
		self.dice=(self.dice[4],self.dice[0],self.dice[2],
					self.dice[3],self.dice[5],self.dice[1])
	def get_top(self, id):
 		return self.dice[id-1]

data=Dice([int(i) for i in sys.stdin.readline().split()])
order=sys.stdin.readline().strip()
for i in order:
	if i=='N':
		data.roll_n()
	elif i=='E':
		data.roll_e()
	elif i=='S':
		data.roll_s()
	elif i=='W':
		data.roll_w()
print(data.get_top(1))