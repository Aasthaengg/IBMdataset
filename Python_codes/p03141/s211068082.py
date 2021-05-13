from collections import deque
N = int(input())
taka = []
ao = []
A = []
B = []
for i in range(N):
    Ain,Bin = map(int,input().split())
    A.append(Ain)
    B.append(Bin)
    taka.append((Bin+Ain,i))
    ao.append((Ain+Bin,i))
taka.sort()
taka.reverse()
ao.sort()
ao.reverse()
taka = deque(taka)
ao = deque(ao)
takacnt = 0
aocnt = 0
st = set()

# print(taka)
# print(ao)

for i in range(N):
    if i % 2 == 0:
        while True:
            val = taka.popleft()
            if not val[1] in st:
                break
        st.add(val[1])
        takacnt += A[val[1]]
    else:
        while True:
            val = ao.popleft()
            if not val[1] in st:
                break
        st.add(val[1])
        aocnt += B[val[1]]
print(takacnt-aocnt)
