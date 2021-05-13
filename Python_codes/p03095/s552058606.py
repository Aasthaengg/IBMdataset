n = int(input())
s = input()
mod = 10**9+7
data = {}
for i in s:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1
ans = 1
for i in data.values():
    ans *= i+1
    ans %= mod
print(ans-1)