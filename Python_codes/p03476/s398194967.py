Q = int(input())

is_prime = [True] * 100010
for i in range(100010):
    if i <= 1:
        is_prime[i] = False
        continue

    if is_prime[i]:
        for j in range(2*i,100010,i):
            is_prime[j] = False

is_2017like_prime = [False] * 100010
for i in range(1,100010,2):
    if is_prime[i] & is_prime[(i+1)//2]:
        is_2017like_prime[i] = True

cumsum = [0]
for a in is_2017like_prime[1:]:
    cumsum.append(cumsum[-1] + a)

for _ in range(Q):
    l, r = map(int,input().split())
    print(cumsum[r]-cumsum[l-1])