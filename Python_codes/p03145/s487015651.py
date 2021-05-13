from sys import stdin
def main():
	readline=stdin.readline
	c,a,b=map(int,readline().split())
	print(c*a//2)
if __name__=="__main__":
	main()