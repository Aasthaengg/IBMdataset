
def main():
	n = int(input())
	arr = list(map(int , input().split()))
	for i in range(0 , n):
		arr[i]=arr[i]-(i+1)
	ans=0
	md=0
	arr.sort()
	if n%2==0:
		md = (arr[n//2-1]+arr[(n//2)])//2
	else:
		md = arr[n//2]
	for i in range(0,n):
		ans = ans +abs(arr[i]-md)
	print(ans)
if __name__=="__main__":
	main()