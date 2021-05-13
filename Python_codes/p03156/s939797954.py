N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
A_list,B_list,C_list = list(),list(),list()

for i in range(len(P)):
	if P[i] <= A:
		A_list.append(P[i])
	elif A+1<=P[i] and P[i] <= B:
		B_list.append(P[i])
	else:
		C_list.append(P[i])
		
print(min(len(A_list),len(B_list),len(C_list)))