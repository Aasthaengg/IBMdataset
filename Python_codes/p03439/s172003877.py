N = int(input())

def ask(n) :
    print(n, flush=True)
    s = input()
    if s == "Vacant" :
        exit()
    return s

def condition(L,R,resp_L, resp_R) :
    if (R-L)%2 == 1 :
        return resp_L == resp_R
    else :
        return resp_L != resp_R

resp = ask(0)

L = 0
R = N
resp_L = resp_R = resp

for i in range(19) :
    M = (L+R)//2
    resp_M = ask(M)
    if condition(L,M,resp_L,resp_M) :
        R,resp_R = M,resp_M
    else :
        L,resp_L = M,resp_M
