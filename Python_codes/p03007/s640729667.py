from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
A.sort()
ans = []
p = A[0]
q = A[-1]
for i in A[1:-1]:
    if i < 0:
        ans.append((q,i))
        q -= i
    else:
        ans.append((p,i))
        p -= i
ans.append((q,p))
print(q-p)
for i,j in ans:
    print(i,j)