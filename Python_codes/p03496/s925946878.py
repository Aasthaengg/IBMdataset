I = int(input())
L = list(map(int, input().split()))

print(2*I-1, flush=True)

m = 0
m_index = 0
for i, item in enumerate(L):
    if abs(item) > abs(m):
        m = item
        m_index = i

for i in range(I):
    print(m_index+1, i+1, flush=True)

if m >= 0:
    for i in range(0, I-1):
        print(i+1, i+2)
else:
    for i in range(I, 1, -1):
        print(i, i-1)
