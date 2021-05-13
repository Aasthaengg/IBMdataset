N=int(input())

M=[]

for i in range (1,N):
    if N-i!=i:
        M.append(N-i)

print(len(M)//2)