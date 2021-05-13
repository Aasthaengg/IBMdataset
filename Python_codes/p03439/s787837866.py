N = int(input())

def ask(n):
    print(n, flush=True)
    resp = input().rstrip()[0]
    if resp == 'V':
        exit()
    return resp

def condition(L,R,resp_L,resp_R):
    if (R-L)&1:
        return resp_L == resp_R
    else:
        return resp_L != resp_R

resp = ask(0)

L = 0
R = N
resp_L = resp
resp_R = resp
for _ in range(19):
    M = (L + R) // 2
    resp_M = ask(M)
    if condition(L,M,resp_L,resp_M):
        R,resp_R = M,resp_M
    else:
        L,resp_L = M,resp_M
