N,M = map(int,input().split())


#print(A)
def comp(lst1,lst2):
    ret = []
    for i in lst1:
        if i in lst2:
            ret.append(i)
    return ret
ret = list(map(int,input().split()))
ret = ret[1:]
#print(ret)
for i in range(1,N):
    lst = list(map(int,input().split()))
    ret = comp(ret,lst[1:])
    #print(ret)
print(len(ret))