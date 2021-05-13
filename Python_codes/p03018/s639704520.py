# move all A's to the back whenever you see ABC i.e it becomes BCA
# Example ABCBCBC after operation it becomes BCBCBCA
# Count the consecutive no of BC and whenever u see a A add the count to answer that many moves required to move A to last
# if it's not A or any other string make cnt as 0
def main():
	s = input()
	cnt = 0
	prev =0
	ans = 0
	i = len(s)-1
	while i>=0:
		if s[i]=='C' and s[i-1]=='B':
			cnt = cnt+1
			i = i-2
		else:
			if s[i]=='A':
				ans = ans+cnt
			else:
				cnt = 0
			i = i-1
	print(ans)
if __name__=="__main__":
	main()