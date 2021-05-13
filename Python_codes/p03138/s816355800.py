import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
a1 = max(A)
n = int(math.log2(max(a1,K)))+1
B = [0 for _ in range(n)]
for i in range(N):
    a = bin(A[i])[2:]
    for j in range(len(a)):
        if a[len(a)-1-j]=="1":
            B[j] += 1
x = bin(K)[2:]
y = ""
flag = 0
for i in range(len(x)):
    if flag==0:
        if x[i]=="0":
            y += x[i]
        else:
            if B[len(x)-1-i]<=N//2:
                y += x[i]
            else:
                y += "0"
                flag = 1
    else:
        if B[len(x)-1-i]<=N//2:
            y += "1"
        else:
            y += "0"
y = int(y,2)
cnt = 0
for i in range(N):
    cnt += y^A[i]
print(cnt)