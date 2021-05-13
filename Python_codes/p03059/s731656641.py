A, B, T = map(int, input().split())
sum = 0
for i in range(0,T+1,A):
    if i == 0:
        continue
    sum += B
print(sum)
