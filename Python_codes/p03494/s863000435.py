N = int(input())
A = list(map(int,(input().split())))

count = 0
is_continue = True
while(True):
    for i in A:
        if(i % 2 != 0):
            is_continue = False
            break
        if(i == 0):
            is_continue = False
            break

    if(is_continue == False):
        break
    else:
        counter = 0
        for i in A:
            A[counter] = i/2
            counter+=1   
    count += 1    
    
print(count)