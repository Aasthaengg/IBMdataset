n=int(input())
l_list=[int(i) for i in input().split()]
l_list.sort()

count=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            li=l_list[i]
            lj=l_list[j]
            lk=l_list[k]
            if li!=lj and li!=lk and lj!=lk:
                if lk<li+lj:
                    count+=1
            
print(count)
