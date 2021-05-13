import collections
n,rev,q = int(raw_input()) ,False,collections.deque()

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

head = None
tail = None
for ai in map(int, raw_input().split()):
	if head is None:
		node = Node(ai)
		head = node
		tail = node
	else:
		node = Node(ai)
		if rev:
			head.prev = node
			node.next= head
			head = node
		else:
			tail.next = node
			node.prev=  tail
			tail = node
		rev ^=  True

cur = head 
temp = []
while(cur):
	temp.append(cur.val)
	cur = cur.next 
print ' '.join(map(str, temp[::-1 if rev else 1]))