n = input()
a_list = map(int,raw_input().split())
a_list.sort()
sum = 0
for i in a_list :
	sum += i
print'%d %d %d' %(a_list[0],a_list[-1],sum)