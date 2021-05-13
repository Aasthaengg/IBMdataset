# coding : utf-8
class Dice:
	def __init__(self, label):
		self.d = label

	def north(self):
		d = self.d
		self.d = [d[1],d[5],d[2],d[3],d[0],d[4]]
	
	def east(self):
		d = self.d
		self.d = [d[3],d[1],d[0],d[5],d[4],d[2]]
	
	def west(self):
		d = self.d
		self.d = [d[2],d[1],d[5],d[0],d[4],d[3]]
	
	def south(self):
		d = self.d
		self.d = [d[4],d[0],d[2],d[3],d[5],d[1]]

	def output(self):
		d = self.d
		print(self.d[0])

label = list(map(int, input().split()))
op_list = list(input())
d0 = Dice(label)
for op in op_list:
	if op =='N':
		d0.north()
	if op =='E':
		d0.east()
	if op =='W':
		d0.west()
	if op =='S':
		d0.south()
d0.output()