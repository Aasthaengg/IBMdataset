N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

if T[-1] != A[0]:
    print(0)
    exit()

max_h = [1] * N

#max_h[0] = T[0]
#max_h[-1] = A[-1]

h = [None] * N
#Tから見ていく
for i in range(1,N-1):

        ht = ha = None
        if T[i] > T[i-1]:
            ht = T[i]
        if A[i] > A[i+1]:
            ha = A[i]

        if ht != None and ha != None:
            if ht == ha:
                h[i] = ht
            else:
                print(0) # 矛盾するので終わり
                exit()
        
        elif ht != None:
            if A[i] < ht:
                print(0) # 矛盾するので終わり
                exit()
            #h[i] = ht
        elif ha != None:
            if T[i] < ha:
                print(0) # 矛盾するので終わり
                exit()
            #h[i] = ha
        

        elif ht == None and ha == None:
            max_h[i] = min(T[i], A[i])


MOD = 10**9 + 7
def mul(a, b):
    return ((a % MOD) * (b % MOD)) % MOD
ans = 1
for i in range(N):
    ans = mul(ans, max_h[i])
    #ans *= max_h[i]

print(ans)