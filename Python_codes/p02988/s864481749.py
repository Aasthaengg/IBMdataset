n = int(input())
assert n <= 20 and n >= 3,"input error(3 <= n <= 20)"
p = list(map(int,input().split()))
res = 0
for i in range(1,n-1,1):
    if (p[i-1] < p[i] and p[i] < p[i+1]) or (p[i-1] > p[i] and p[i] > p[i+1]):
        res +=1

print(res)