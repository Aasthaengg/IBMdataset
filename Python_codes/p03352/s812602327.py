import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()


def main():
	x=II()

	li=set([1])

	for i in range(2,35):
		for j in range(2,11):
			if i**j<=1001:
				li.add(i**j)
			else:
				break

	li=list(li)
	li.sort(reverse=True)

	#print(li)

	for i in li:
		if i<=x:
			print(i)
			exit()










if __name__ == "__main__":
	main()
