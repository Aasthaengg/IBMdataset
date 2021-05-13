n = int(input())
s = input()
count = [0]*26
for i in s:
    count[ord(i)-ord("a")] += 1
mod = 10**9+7
ans = 1
for i in count:
    ans *= (i+1)
    ans %= mod
print(ans-1)