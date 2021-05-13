from collections import deque
N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
B = [0]*M
dic = {}
for i in range(M):
    c,b = list(map(int,input().split()))
    B[i] = b
    if dic.get(b):dic[b] += c
    else:dic[b] = c
# print(dic)
A = deque(sorted(A))
B = deque(sorted(list(set(B)),reverse=True))
C = []

while A:
    b = B[0]
    if A[0]<b:
        A.popleft()
        C.append(b)
        dic[b] -= 1
        if dic[b]==0:
            B.popleft()
            if not B:break
    else:break
# print(dic[C[0]])
print(sum(A)+sum(C))