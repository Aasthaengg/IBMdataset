def main():
	a,b , c = map(int , input().split())
	ans = a*b*c
	ans = min(ans, abs(b*c*((a//2)-(a-(a//2)))))
	ans = min(ans, abs(a*c*((b//2)-(b-(b//2)))))
	ans = min(ans, abs(b*a*((c//2)-(c-(c//2)))))
	print(ans)
if __name__=="__main__":
	main()