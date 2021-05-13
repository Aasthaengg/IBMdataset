import os
import sys

def main():
	a,b,c = map(int, input().split())
	if a+b+c >= 22:
		print("bust")
		sys.exit()
	else:
		print("win")
		sys.exit()

if __name__ == "__main__":
	main()
