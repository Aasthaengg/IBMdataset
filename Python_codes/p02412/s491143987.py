while True :
	n,x=map(int,raw_input().split())
	if not( n==0 and x==0) :
		p_count = 0
		i,j,k = [1,2,3]
		while i <= n-2 :
			j = i+1
			while j <= n-1:
				k = j+1
				while k <= n:
					if (i+j+k)==x :
						p_count += 1
						k += 1
						break
					else :
						k += 1
				j += 1
			i += 1
		print(p_count)
 	else :
 		break