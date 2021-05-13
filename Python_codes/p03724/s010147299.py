# code like professional "write main function"
def main():
	# we can always make a tree from the given set of nodes what we like
	# any possible tree
	n , m = map(int , input().split())
	deg = [0 for i in range(n+2)]
	for i in range(m):
		x , y = map(int , input().split())
		deg[x]+=1
		deg[y]+=1
	f=0
	# traversing a node would add 1 to one of its outgoing edges
	# if the out going edges need to have 0 parity than it should occur even no ot times
	for i in range(1, n+1):
		if deg[i]%2==1:
			f = 1
	if f:
		print("NO")
	else:
		print("YES")
if __name__=="__main__":
	main()