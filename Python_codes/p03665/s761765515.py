import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    N,P = map(int,input().split())
    A = list(map(int,input().split()))
    num1 = 0
    num0 = 0
    for i in range(N):
        tmp = A[i]%2
        if tmp == 0:
            num0 += 1
        else:
            num1 += 1
    #print(num1,num0)
    ans2 = 0
    for i in range(num0+1):
        ans2 += comb(num0,i)

    if P == 1:
        syo = num1//2
        amari = num1%2
        tmp = syo + amari
        i = 1
        ans = 0
        for j in range(tmp):
            ans += comb(num1,i)
            i += 2


        ans = ans*ans2
        return ans

    else:
        syo = num1//2
        tmp = syo+1
        i = 0
        ans = 0
        #print(tmp)
        for j in range(tmp):
            #print(i,num1)
            if i == 0:
                ans += 1
                i += 2
            else:
                ans += comb(num1,i)
                i += 2

        ans = ans*ans2
        return ans

#print(comb(3,2))
print(main())
