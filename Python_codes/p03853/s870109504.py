[h,w]=list(map(int,input().split()))
#print(h,w)
lst=[]
for i in range(h):
    lst.append(input())
#print(lst)

lst2=[]
for i in range(h*2):
    lst2.append(lst[i//2])
#print(lst2)
for i in lst2:
    print(i)