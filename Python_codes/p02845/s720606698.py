n = int(input())
a = list(map(int, input().split()))

h = [0 for _i in range(n)]+[3]
result = 1
mod = 10**9 +7
for i in a:
    result = (result*(h[i-1]-h[i]))%mod
    h[i] += 1
print(result)