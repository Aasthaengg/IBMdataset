N ,K = map(int ,input().split())
num = set()
for i in range(K):
    d = input()
    num.update(int(x) for x in input().split())

sum = 0
for k in num:
    sum += 1
print(N-sum)    
