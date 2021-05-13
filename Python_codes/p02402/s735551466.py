n = input()
a_list = map(int, raw_input().split())

def add(x, y):
	return x+y
	
print "%d %d %d" % (min(a_list), max(a_list), reduce(add, a_list))