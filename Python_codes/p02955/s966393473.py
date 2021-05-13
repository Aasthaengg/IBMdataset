import math
N,K = map(int,input().split())
A_s = list(map(int,input().split()))
S = sum(A_s)
divs = []
for i in range(1, round(math.sqrt(S)+1) ):
    if S%i==0:
        divs.append(i)
        divs.append(S//i)
answer = 1
for div in divs:
    r_s = []
    for A in A_s:
        r_s.append(A%div)
    r_s.sort()
    if sum(r_s[:-sum(r_s)//div]) <= K and answer < div:
        answer = div
    # for i,r in enumerate(r_s[-sum(r_s)//div:]):
    #     r_s[i] = 

print(answer)