Q = int(input())

ls = [list(map(int,input().split())) for i in range(Q)]

n_max = 10**5

prime = []
data = [i for i in range(2,n_max+1)]
limit = n_max**(1/2)

while True:
    p = data[0]
    if limit<=p:
        break
    prime.append(p)
    data = [i for i in data if i%p!=0]

prime = prime +data

ans_ls = [0]*(1+n_max)
for i in prime:
    if (i + 1) // 2 in prime:
        ans_ls[i] = 1

ans_cs = [0]*(1+n_max)
for i in range(n_max):
    ans_cs[i+1] = ans_cs[i]+ans_ls[i+1]
    
for l,r in ls:
    print(ans_cs[r]-ans_cs[l-1])


