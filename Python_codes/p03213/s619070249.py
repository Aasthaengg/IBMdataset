primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

N = int(input())

prime_sep = []

bigger_than4 = []
bigger_than2 = []
bigger_than74 = []
bigger_than14 = []
bigger_than24 = []

for i in primes:
    tmp = N
    if tmp//i > 0:
        count = 0
        while tmp//i > 0:
            tmp = tmp//i
            count+=tmp
        prime_sep.append([count,i])
        if count >= 4:
            bigger_than4.append([count,i])
        if count >= 2:
            bigger_than2.append([count,i])
        if count >=74:
            bigger_than74.append([count,i])
        if count >= 14:
            bigger_than14.append([count,i])
        if count >= 24:
            bigger_than24.append([count,i])

def nCr(n,r):
    if r > n:
        return 0
    ans = 1
    for i in range(n,n-r,-1):
        ans = ans*i
    for i in range(1,r+1,1):
        ans = ans//i
    return ans

res = nCr(len(bigger_than2)-len(bigger_than4),1)*nCr(len(bigger_than4),2) + 3*nCr(len(bigger_than4),3)
res+= nCr(len(bigger_than4)-len(bigger_than14),1)*nCr(len(bigger_than14),1) + 2*nCr(len(bigger_than14),2)
res+= nCr(len(bigger_than2)-len(bigger_than24),1)*nCr(len(bigger_than24),1) + 2*nCr(len(bigger_than24),2)
res+= len(bigger_than74)
print(res)