n=int(input())
mochi_list=[int(input())for i in range(n)]
#print(mochi_list)
kakagamimochi_list=list(set(mochi_list))
print(len(kakagamimochi_list))