
def main():
	h , w = map(int , input().split())
	ls =[]
	ans = []
	for i in range(0 ,h):
		ls.append(list(map(int , input().split())))
	for i in range(0 , h):
		for j in range(0 , w-1):
			if ls[i][j]%2==1:
				ls[i][j+1]+=1
				ans.append([i+1, j+1, i+1, j+2])
	for i in range(h-1):
		if ls[i][-1]%2==1:
			ls[i+1][-1]+=1
			ans.append([i+1,  w, i+2 , w])
	print(len(ans))
	for i in ans:
		print(*i)
if __name__=="__main__":
	main()