def strToList(str,offset=0):
    res = [];
    for el in str.split(" "):
        if el!='':
            res.append(int(el)+offset)
    return res


[N,M,K] = strToList(input())
A = strToList(input())
B = strToList(input())

current_time = 0
current_value = 0
iA = 0
iB = 0

while iA<N:
    if current_time+A[iA]<=K:
        current_time+=A[iA]
        current_value+=1
        iA+=1
    else:
        break

max_value = current_value
iA-=1

while iA>-2 and iB<M:
    if current_time+B[iB]<=K:
        current_time+=B[iB]
        iB+=1
        current_value+=1
        if current_value>max_value:
            max_value=current_value
    else:
        current_time-=A[iA]
        iA-=1
        current_value-=1

print(max_value)
