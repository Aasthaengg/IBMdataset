if __name__ == '__main__':
	N = int(input())
	s = input()
	total = len(s)
	cnt=0
	for si in s:
		if si == 'R' : cnt+=1
	if(total-cnt < cnt):print("Yes")
	else:print("No")