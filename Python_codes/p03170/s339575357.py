import sys
import unittest

class Solution(object):
	def __init__(self):
		self.n = 0
		self.k = 0
		self.a = []
		
	def readInput(self):
		a = sys.stdin.readline().split()
		self.n = int(a[0])
		self.k = int(a[1])
		a = sys.stdin.readline().split()
		for i in xrange(self.n):
			self.a.append(int(a[i]))
		
	def findWinner(self):
		dp = [False] * (self.k + 1)
		for i in xrange(self.k+1):
			for j in xrange(self.n):
				if i >= self.a[j] and not dp[i-self.a[j]]:
					dp[i] = True
		print "First" if dp[self.k] else "Second"
	
	
if __name__ == '__main__':
	s = Solution()
	s.readInput()
	s.findWinner()
