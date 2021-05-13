N,K = list(map(int,input().split()))
# N = random.randint(1,20)
# K = random.randint(1,N)
# print(N,K)

p=(10**9)+7

def get_mod_factalize(A):
    a_mod = 1     
    for a in range(1,A+1):
        a_mod = a * a_mod % p
    return a_mod

def get_mod_comb(A,B):
    a_mod = get_mod_factalize(A)
    b_mod = get_mod_factalize(B)
    a_b_mod = get_mod_factalize(A-B)

    return (a_mod * pow((b_mod*a_b_mod),p-2,p))%p

a = N-K
b = K

for i in range(1,K+1): 
    if i > a+1 :
        ans=0
    else:
        ans=(get_mod_comb(a+1,i) * get_mod_comb(b-1,i-1))%p
    print(ans)