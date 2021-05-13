A, B, K = map(int, input().split())
count = 0
while count<K:
    if count%2==0:
        if A%2==0:
            A//=2
            B+=A
        else:
            A-=1
            A//=2
            B+=A
    else:
        if B%2==0:
            B//=2
            A+=B
        else:
            B-=1
            B//=2
            A+=B
    count+=1
print(A,B)