import collections
n,rev = int(raw_input()) ,False
class Node(object):
	def __init__(self, val):
		self.val = val
		self.next, self.prev = None, None

for i,ai in enumerate(map(int, raw_input().split())):
	node = Node(ai)		
	if i  == 0:
		head,tail = node,node
	else:
		if rev:
			head.prev, node.next = node, head
			head = node
		else:
			tail.next, node.prev = node, tail
			tail = node
		rev ^=  True

cur = head if not(rev) else tail  
while(cur):
	print cur.val, 
	cur = cur.next if not(rev) else cur.prev
