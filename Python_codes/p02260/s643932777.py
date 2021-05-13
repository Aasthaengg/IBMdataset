def selection_sort(List):
	cnt = 0
	l=len(List)
	for i in range(l):
		num_index=i
		for j in range(i,l):
			if List[num_index]>List[j]:
				num_index=j
		if num_index != i:
			temp=List[num_index]
			List[num_index]=List[i]
			List[i]=temp
			cnt+=1
	return cnt
N=input()
N_List=map(int,raw_input().split())
cnt=selection_sort(N_List)
print(" ".join(map(str,N_List)))
print(cnt)