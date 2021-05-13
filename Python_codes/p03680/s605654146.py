N = (int(input()))
A = [0]+[int(input()) for T in range(0,N)]
Now = 1
Count = 0
Flag  = False
for T in range(0,N):
    Next = A[Now]
    Count += 1
    if Next==2:
        Flag = True
        break
    else:
        Now = Next
if Flag:
    print(Count)
else:
    print(-1)