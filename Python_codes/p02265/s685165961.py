class MyList:
	head = tail = None

	def insert(self, x):
		n = [x, None, None]
		if self.head == None:
			self.head = self.tail = n
		else:
			n[2] = self.head
			self.head[1] = n
			self.head = n

	def delete(self, x):
		n = self.head
		while n and n[0] != x:
			n = n[2]
		if n: 
			self.__delete_node(n)

	def deleteFirst(self):
		self.__delete_node(self.head)

	def deleteLast(self):
		self.__delete_node(self.tail)

	def __delete_node(self, n):
		if n == self.head:
			self.head = n[2]
		if n == self.tail:
			self.tail = n[1]
		if n[1]:
			n[1][2] = n[2]
		if n[2]:
			n[2][1] = n[1]

	def print_all(self):
		n = self.head
		while n:
			print n[0],
			n = n[2]

myList = MyList()
n = int(raw_input())
for _ in xrange(n):
	line = raw_input()
	if line[0]=='i':
		myList.insert(line[7:])
	elif line[6]=='F':
		myList.deleteFirst()
	elif line[6]=='L':
		myList.deleteLast()
	else:
		myList.delete(line[7:])
myList.print_all()