N = int(input())
S = "abcdefghijklmn"
Q = [(1,1,"a")]
A = []
while Q:
    q = Q.pop(-1)
    if q[0]==N:
        A.append(q[2])
        continue
    for i in range(q[1]+1):
        Q.append((q[0]+1,max(q[1],i+1),q[2]+S[i]))
for a in sorted(A):print(a)