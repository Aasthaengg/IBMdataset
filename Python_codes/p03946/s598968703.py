N,T = map(int,input().split())
A_s = list(map(int,input().split()))
MIN = A_s[0]
DIVS = []
for A in A_s:
    if MIN > A:
        MIN = A
    DIVS.append(A-MIN)
MAX = max(DIVS)
answer = DIVS.count(MAX)
print(answer)