import copy
 
N,M,X = map(int,input().split())
 
res = 10**8
 
C = [0] * N
A = [0] * N
 
for i in range(N):
    L = list(map(int,input().split()))
    C[i] = L[0]
    A[i] = L[1:]
 
def check_x(a):
    for i in range(len(a)):
        if a[i] < X:
            return False
    return True
 
# n…2^12(12bit)の整数
def calc_money_under(n):
    global res

    understand = [0] * M
    money = 0
    for s in range(N):
        if (n >> s) & 1:
            money += C[s]
            for j in range(M):
                understand[j] += A[s][j]
            #print(understand)
    
    if check_x(understand):
        res = min(money, res)
    return
 
for n in range(2**N):
    calc_money_under(n)
 
if res == 10**8:
    print(-1)
else:
    print(res)