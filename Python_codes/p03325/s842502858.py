import collections
N = int(input())
A = filter(lambda x: x%2 == 0,map(int,input().split()))
C = collections.Counter(A)
ans = 0
for key in C.keys():
    tmp = key
    count = 0
    while tmp%2 == 0:
        tmp //= 2
        count += 1
    ans += C[key]*count
print(ans)