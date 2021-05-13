N=int(input())
A=sorted(list(map(int,input().split(' '))))
acc=[A[0]]
ans =1
for i in A[1:]:
    acc.append(acc[-1]+i)
for i in range(N-1,0,-1):
    if A[i]>acc[i-1]*2:
        print(N-i)
        exit()
print(N)