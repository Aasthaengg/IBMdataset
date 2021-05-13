a1=input()
b1=input()
N=len(a1)
n=0
for i in range(N):
    if a1[i]!=b1[i]:
        n+=1
print(n)