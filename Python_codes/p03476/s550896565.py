q = int(input())
Q = 10**5+1
is_prime = [1] * (Q+1)
is_prime[0],is_prime[1] = 0,0
for i in range(2,int(Q*0.5)+1):
    if is_prime[i]:
        product = i*2
        while product <= Q:
            is_prime[product] = 0
            product += i
is_2017_like = [0] * (Q+1)
is_2017_like_csum = [0] * (Q+1)
now = 0
for i in range(2,Q+1):
    if is_prime[i] and is_prime[(i+1)//2]:
        is_2017_like[i] = 1
        now += 1
    is_2017_like_csum[i] = now
ans_ls = [0] * q
for i in range(q):
    l,r = map(int,input().split())
    if l >= 1:
        ans_ls[i] = is_2017_like_csum[r] - is_2017_like_csum[l-1]
    else:
        ans_ls[i] = is_2017_like_csum[r]
for i in range(q):
    print(ans_ls[i])
