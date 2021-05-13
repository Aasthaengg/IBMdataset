S = int(input())
A = [S]
Count = 1
while True:
    Count += 1
    if A[-1]%2==0:
        Next = A[-1]//2
        if Next in A:
            print(Count)
            break
        else:
            A.append(Next)
    else:
        Next = 3*A[-1]+1
        if Next in A:
            print(Count)
            break
        else:
            A.append(Next)