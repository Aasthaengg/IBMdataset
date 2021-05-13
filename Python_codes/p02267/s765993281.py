from collections import deque

def linersearch(A,n,key):
    i = 0
    A.append(key)
    while A[i] != key:
        i += 1
    if i == n:
        A.pop()
        return False
    else:
        A.pop()
        return True

n = int(input())
S = deque([int(x) for x in input().split()])
q = int(input())
T = [int(x) for x in input().split()]
ans = 0

for q in T:
    if linersearch(S,n,q):
        ans += 1

print(ans)
