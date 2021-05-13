N=int(input())
list1=[]
list2=[]
for i in map(int,input().split()):
    if i % 2 == 0:
        list1.append(i)
    if i % 2 == 0 and (i % 3 == 0 or i % 5 ==0):
        list2.append(i)
if list1 == list2:
    print('APPROVED')
else:
    print('DENIED')