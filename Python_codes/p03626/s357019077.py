# code like professional " write main function "

import sys
def main():
	n = int(input())
	S1 =input()
	S2 =input()
	ans  = 1
	mod = 10**9+7
	i = 0
	if S1[0]==S2[0]:
		ans = 3
		i=1
	else:
		ans = 6
		i = 2
	while i<n:
		if S1[i]==S2[i]:
			if S1[i-1]==S2[i-1]:
				ans = (ans*2)%mod
			i = i+1
		else:
			if S1[i-1]==S2[i-1]:
				ans = (ans*2)%mod
			else:
				ans = (ans*3)%mod
			i = i+2
	print(ans)

if __name__ == "__main__":
	main()