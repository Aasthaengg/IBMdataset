n=int(input())

a=[]
a_sort=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
    a_sort.append(tmp)
a_sort.sort(reverse=True)

for i in range(n):
    if a_sort[0]==a[i]:print(a_sort[1])
    else:print(a_sort[0])