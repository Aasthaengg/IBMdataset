#  very slow solution
def main():
	N = int(input())
	for n in range(1, 3502):
		for h in range(1,3502):
			t = n*h*N
			p = 4*n*h-(n*N+h*N)
			if p>0 and t%p==0:
				w = t//p
				print(n , h, w)
				exit()


if __name__=="__main__":
	main()