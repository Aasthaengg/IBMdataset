n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
cnt = 0
for i in T:
    m = 0
    S.append(i)
    while i != S[m]:
        m+=1
    if m != n:
        cnt+=1
    S.pop()
print(cnt)
