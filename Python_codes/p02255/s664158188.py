length=int(input())
firstArray=input()
listForArray=list(map(int,firstArray.split()))
listForPrint=[firstArray]


def insertionSort(list,length):
    index=1
    while index<length:
        if listForArray[index]<=listForArray[index-1]:
            for index2 in range(0,index):
                if listForArray[index2-1]<=listForArray[index] and listForArray[index]<=listForArray[index2] or index2==0 and listForArray[index]<=listForArray[index2]:
                    newCommer=listForArray[index]
                    n=index
                    while n>index2:
                        listForArray[n]=listForArray[n-1]
                        n-=1
                    listForArray[index2]=newCommer
                    break   
        nowArray=str(listForArray[0])
        for index3 in range(1,length):
            nowArray+=" "+str(listForArray[index3])
        listForPrint.append(nowArray)
        index+=1    
#---------------------main-------------------------
insertionSort(listForArray,length)
for array in listForPrint:
    print(array)
