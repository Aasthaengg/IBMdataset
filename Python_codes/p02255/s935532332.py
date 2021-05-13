import copy

def insertion_sort(List):
	l=len(List)
	for i in range(l):
		for j in range(i):
			if List[i]<List[j]:
				temp=copy.copy(List)
				for k in range(j,i):
					List[k+1]=temp[k]
				List[j]=temp[i]
				break
		print(" ".join(map(str,List)))

N=input()
N_List=map(int,raw_input().split())
insertion_sort(N_List)