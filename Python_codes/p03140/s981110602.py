n = int(input())
listA = list(input())
listB = list(input())
listC = list(input())


counter=0
index=0
while index < n:
    if listA[index] == listB[index] and listB[index] == listC[index]:
        pass
    elif listA[index] != listB[index] and listB[index] != listC[index] and listC[index]!=listA[index]:
        counter+=2
    else:
        counter+=1
    index+=1
print(counter)