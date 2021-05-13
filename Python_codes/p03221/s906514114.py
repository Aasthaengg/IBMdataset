n,m=map(int,input().split())
py1=[]
for i in range(m):
    py1.append(list(map(int,input().split()))+[i+1])
py=sorted(py1)

number_list=[]
number_list.append([str(0)]*(6-(len(list(str(py[0][0])))))+list(str(py[0][0]))+[str(0)]*(6-(len(list(str(1)))))+list(str(1))+[str(py[0][-1])])
k=2
for j in range(1,m):
    if py[j][0]==py[j-1][0]:
        number_list.append([str(0)]*(6-(len(list(str(py[j][0])))))+list(str(py[j][0]))+[str(0)]*(6-(len(list(str(k)))))+list(str(k))+[str((py[j][-1]))])    
        k+=1
    else:
        k=1
        number_list.append([str(0)]*(6-(len(list(str(py[j][0])))))+list(str(py[j][0]))+[str(0)]*(6-(len(list(str(k)))))+list(str(k))+[str(py[j][-1])])
        k+=1
     
number_list_sort=sorted(number_list,key=lambda x:int(x[-1]))
for l in range(m):
    print(''.join(number_list_sort[l][:-1]))