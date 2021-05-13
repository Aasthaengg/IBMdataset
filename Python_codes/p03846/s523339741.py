N = int(input())
A = list(map(int, input().split()))
B=[]
if N%2 ==0:
    for a in range(1, N, 2):
        B.append(a)
    B+=B
    if sorted(A) == sorted(B):
        print(2**len(set(A))%(10**9+7))
    else:
        print(0)
else:
    for a in range(2, N, 2):
        B.append(a)
    B=B+B+[0]
    if sorted(A) == sorted(B):
        print(2**(len(set(A))-1)%(10**9+7))
    else:
        print(0)