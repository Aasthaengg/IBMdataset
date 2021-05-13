class Dice():
	def __init__(self):
		self.number = [_ for _ in range(6)]
		self.work = [_ for _ in range(6)]

	def setNumber(self,n0,n1,n2,n3,n4,n5):
		self.number[0] = n0
		self.number[1] = n1
		self.number[2] = n2
		self.number[3] = n3
		self.number[4] = n4
		self.number[5] = n5

	def roll(self,loc):
		for _ in range(6):
			self.work[_] = self.number[_]
		if loc == "E":
			self.setNumber(self.work[3],self.work[1],self.work[0],self.work[5],self.work[4],self.work[2])
		elif loc == "N":
			self.setNumber(self.work[1],self.work[5],self.work[2],self.work[3],self.work[0],self.work[4])
		elif loc == "S":
			self.setNumber(self.work[4],self.work[0],self.work[2],self.work[3],self.work[5],self.work[1])
		elif loc == "W":
			self.setNumber(self.work[2],self.work[1],self.work[5],self.work[0],self.work[4],self.work[3])
	def get_top(self):
		return self.number[0]
	def get_right(self,n1,n2):
		if(n1 == self.number[0]):
			if(n2 == self.number[1]): print(self.number[2])
			elif(n2 == self.number[2]): print(self.number[4])
			elif(n2 == self.number[3]): print(self.number[1])
			elif(n2 == self.number[4]): print(self.number[3])
		elif(n1 == self.number[1]):
                        if(n2 == self.number[0]): print(self.number[3])
                        elif(n2 == self.number[2]): print(self.number[0])
                        elif(n2 == self.number[3]): print(self.number[5])
                        elif(n2 == self.number[5]): print(self.number[2])
		elif(n1 == self.number[2]):
                        if(n2 == self.number[0]): print(self.number[1])
                        elif(n2 == self.number[1]): print(self.number[5])
                        elif(n2 == self.number[4]): print(self.number[0])
                        elif(n2 == self.number[5]): print(self.number[4])
		elif(n1 == self.number[3]):
                        if(n2 == self.number[0]): print(self.number[4])
                        elif(n2 == self.number[1]): print(self.number[0])
                        elif(n2 == self.number[4]): print(self.number[5])
                        elif(n2 == self.number[5]): print(self.number[1])
		elif(n1 == self.number[4]):
                        if(n2 == self.number[0]): print(self.number[2])
                        elif(n2 == self.number[2]): print(self.number[5])
                        elif(n2 == self.number[3]): print(self.number[0])
                        elif(n2 == self.number[5]): print(self.number[3])
		elif(n1 == self.number[5]):
                        if(n2 == self.number[1]): print(self.number[3])
                        elif(n2 == self.number[2]): print(self.number[1])
                        elif(n2 == self.number[3]): print(self.number[4])
                        elif(n2 == self.number[4]): print(self.number[2])

data = list(map(int,input().split()))
q = int(input())

mydice = Dice()

mydice.setNumber(data[0],data[1],data[2],data[3],data[4],data[5])
for _ in range(q):
	flat = list(map(int,input().split()))
	mydice.get_right(flat[0],flat[1])

