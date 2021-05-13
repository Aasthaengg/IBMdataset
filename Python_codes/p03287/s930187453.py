from itertools import *
from collections import *

def main():
	_, m, *c = map(int, open(0).read().split())
	print(sum(x * (x - 1) // 2 for x in Counter([0] + [x % m for x in accumulate(c)]).values()))

if __name__=="__main__":
	main()