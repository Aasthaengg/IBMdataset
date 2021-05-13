N = int(input())
P = [1]*(N+1)
for i in range(1,N+1):
    n = i
    for j in range(2,N+1):
        while n%j==0:
            P[j]+=1
            n//=j
P = [p for p in P if p>1]
N = len(P)-1
cnt = 0
B = [1,3,5,15,25,75]
def f(k,d):
    global N,P,cnt,B
    if d==75:
        cnt += 1
        return
    elif d>75 or k>N:
        return
    for i in range(1,P[k]+1):
        if i in B:
            f(k+1,d*i)
f(0,1)
print(cnt)