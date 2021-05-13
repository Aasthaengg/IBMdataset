hen_list=list(map(int,input().split()))
print(['No','Yes'][hen_list.count(hen_list[0])==3])