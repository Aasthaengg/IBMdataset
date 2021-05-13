import itertools
n,k=map(int, input().split())
A=[int(i) for i in input().split()]
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse = True)
    return divisors
divlis = make_divisors(sum(A))

for res in divlis:
    tmp = [i%res for i in A]
    tmp.sort()
    tmp_l = [0]+list(itertools.accumulate(tmp))
    tmp_r = [0]*(n+1)
    
    for i in range(n-1,-1,-1):
        tmp_r[i] = tmp_r[i+1] + res-tmp[i]

    for i in range(n+1):
        if(tmp_l[i]==tmp_r[i] and tmp_l[i]<=k):
            print(res)
            exit()
