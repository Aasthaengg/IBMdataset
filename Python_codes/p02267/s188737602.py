n_1=input()
n_1_List=map(int,raw_input().split())
n_2=input()
n_2_List=map(int,raw_input().split())
n_1_List=set(n_1_List)
n_2_List=set(n_2_List)
print(len(n_1_List.intersection(n_2_List)))