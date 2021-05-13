sticks=int(input())
lengths=input()
new_list=lengths.split()
list=[]
for item in new_list:
    list.append(int(item))
i=len(list)-1
j=i-1
k=i-2
count=0
empty=[]
while i>=2:
    while j>=1:
        while k>=0:
            if list[i]!=list[j]and list[i]!=list[k]and list[j]!=list[k]:
                empty.append((list[i],list[j],list[k]))
            k=k-1
        j=j-1
        k=j-1
    i=i-1
    j=i-1
    k=j-1
for items in empty:
    if items[0]+items[1]>items[2]and items[1]+items[2]>items[0]and items[2]+items[0]>items[1]:
        count=count+1
print(count)