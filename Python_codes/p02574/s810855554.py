N = int(input())
A = list(map(int, input().split()))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)    

table = [0] * (10**6+5)

pairwise_flg = True
for num in A:
    table[num] += 1

for i in range(2, 10**6+5):
    cnt = 0
    for j in range(i, 10**6+5, i):
        cnt += table[j]
    if cnt > 1:
        pairwise_flg = False    
if pairwise_flg:
    print("pairwise coprime")
    exit()

gcd_val = 0
for num in A:
    gcd_val = gcd(gcd_val, num)

if gcd_val == 1:
    print("setwise coprime")
    exit()
print("not coprime")    