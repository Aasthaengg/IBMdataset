from collections import deque
N = int(input())
lis = []

A = []
B = []
for i in range(N):
    Ain,Bin = map(int,input().split())
    A.append(Ain)
    B.append(Bin)
    lis.append((Ain+Bin,i))
lis.sort()
lis.reverse()
lis = deque(lis)

takacnt = 0
aocnt = 0
st = set()

# print(taka)
# print(ao)

for i in range(N):
    if i % 2 == 0:
        while True:
            val = lis.popleft()
            if not val[1] in st:
                break
        st.add(val[1])
        takacnt += A[val[1]]
    else:
        while True:
            val = lis.popleft()
            if not val[1] in st:
                break
        st.add(val[1])
        aocnt += B[val[1]]
print(takacnt-aocnt)
