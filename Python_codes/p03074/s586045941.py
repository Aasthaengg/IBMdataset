
# spent 4 hrs for this question why i am noob:(
# group all the consecutive elements and keep a count of each group and type of group whether it's one or zero
# After grouping all the same elements the string would alternate for 0 and 1
# suppose if u are current group of 1 then u need to chose next 2*k group as 0101,010101,01010101 as k is 2, 3, 4 respectively 
# u can flip every consecutive zero's in the above
# suppose if the current group start's with 0 then u need to choose next 2*k-1 groups as 101 , 10101 as k is 2 , 3 respectively
# u can flip every consecutive zero's 
def main():
	n , k = map(int , input().split())
	hd = input()
	grp=[]
	if hd[0]=='1':
		grp = [[0,0]]
	else:
		grp=[[0,0]]
	cnt =1
	for i in range(1, len(hd)):
		if hd[i]==hd[i-1]:
			cnt = cnt+1
		else:
			grp.append([cnt,i])
			cnt = 1
	grp .append([cnt , len(hd)-1])
	pre = [0 for i in range(0 , len(grp)+9)]
	pre[0]=grp[0][0]
	for i in range(1, len(grp)):
		pre[i]=pre[i-1]+grp[i][0]
	ans = 0
	for i in range(0 , len(grp)):
		if hd[grp[i][1]]=='0':
			rgt = min(i+2*k, len(grp)-1)
			ans = max(ans, pre[rgt]-pre[i])
		else:
			rgt = min(i+2*k+1, len(grp)-1)
			ans = max(ans, pre[rgt]-pre[i])
		if rgt==len(grp)-1:
			break
	print(ans)
if __name__=="__main__":
	main()