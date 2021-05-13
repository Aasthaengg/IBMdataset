N = int(input())

a = list(map(int,input().split()))

a_max = max(a)

half_a = a_max//2

comb = 1000000000
for i in range(N):
    if a[i]==a_max:
        continue
    if comb>abs(half_a-a[i]):
        idx =i
        comb = abs(half_a-a[i])

print(str(a_max) + ' ' + str(a[idx]))