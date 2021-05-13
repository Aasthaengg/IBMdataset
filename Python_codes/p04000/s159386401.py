h, w, n = map(int, input().split())

d = {}
ab = []

for i in range(n):
    s = input()
    d[s] = 1
    a, b = map(int, s.split())
    ab.append((a, b))

memo = [0] * 10

def check(a,b):
    cnt = 0
    for i in range(a,a+3):
        for j in range(b,b+3):
            if str(i) + ' ' + str(j) in d:
                cnt += 1
    memo[cnt] += 1
                
for a, b in ab:
    for i in range(max(1,a-2), min(h-1,a+1)):
        for j in range(max(1,b-2), min(w-1,b+1)):
            check(i,j)

for i in range(1, 10):
    memo[i] = memo[i] // i

memo[0] = (h-2) * (w-2) - sum(memo)

for memoi in memo:
    print(memoi)


    


