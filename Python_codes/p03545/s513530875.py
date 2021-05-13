# pro level coding
def main():
	ad = input()
	now = int(ad[0])
	q = []
	n = len(ad)
	q.append([0 , now , ad[0]])
	while len(q)!=0:
		#print(23)
		cur = q.pop(0)
		#print(cur[0] , cur[1] , cur[2])
		if cur[0] ==n-1:
			if cur[1]==7:
				print(cur[2]+'='+'7')
				break
				exit(0)
			continue
		#print(cur[1]+((int)(ad[cur[0]+1])) , cur[0])
		if cur[0]+1<n:
			q.append([cur[0]+1, cur[1]+((int)(ad[cur[0]+1])) , cur[2]+'+'+ad[cur[0]+1]])
			q.append([cur[0]+1, cur[1]-((int)(ad[cur[0]+1])) , cur[2]+'-'+ad[cur[0]+1]])
if __name__=="__main__":
	main()