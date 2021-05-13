N= int(input())
a = [0] * N
b = [0] * N
bi= [0] * N
for i in range(N):
    a[i],b[i]= map(str, input().split())
    bi[i] =int(b[i]) 
X =input()
for j in range(N):
    if X==a[j]:
        B = sum(bi[j+1:])
        print(B)