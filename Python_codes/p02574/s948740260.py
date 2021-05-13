N = int(input())

A = list(map(int, input().split()))

def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

freq = [0] * 1000005

for i in range(len(A)):
    freq[A[i]] += 1

pairwise = True

for i in range(2, 1000005):
    cnt = 0
    for j in range(i, 1000005, i):
        cnt += freq[j]
    # 2箇所以上に素因数が現れたら、pairwiseではない    
    if cnt > 1:
        pairwise = False

if pairwise:
    print("pairwise coprime")
    exit()

g = A[0]
for i in range(1, len(A)):
    g = gcd(g,A[i])
if g == 1:
    print("setwise coprime")
    exit()
    
print("not coprime")


