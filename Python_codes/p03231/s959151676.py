from fractions import gcd
n,m = map(int,input().split())
s = input()
t = input()

len_x = n*m//gcd(n,m)

li = set([i*(len_x//n)+1 for i in range(n)])&set([j*(len_x//m)+1 for j in range(m)])

for l in li:
    if s[(l-1)//(len_x//n)]!=t[(l-1)//(len_x//m)]:
        print(-1);exit()
print(len_x)