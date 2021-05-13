
S = input().split(" ")
N = int(S[0])
M = int(S[1])

def calculate(n,m,baseP,i):

    s = (0.5 ** m)
    successP = s * baseP
    failureP = baseP * (1 - s)

    time =  successP * ( (n - m) * 100 + m * 1900) * i

    if successP < 1e-9:
        return time
    else:
        return time + calculate(n,m,failureP,i+1)


result = calculate(N,M,1,1)
print(round(result))
