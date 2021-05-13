n = int(input())
count =0
store_list=[]
dictA={}
ans_list=[1]*n
for _ in range(n):
    s = input()
    s_list = list(s)
    s_list.sort()
    a =tuple(s_list)
    dictA.setdefault(a,0)
    dictA[a] +=1 
    #print(dictA)
#print(sum(ans_list))
total = 0
for value in dictA.values() :
    total += value*(value-1)/2
       
print(int(total))