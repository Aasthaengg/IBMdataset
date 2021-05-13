n = int(input())
s = input()
li = [1]*26
for c in s:
    li[ord(c)-ord('a')] += 1
ans = 1
for i in li:
    ans *= i
ans -= 1
print(ans%(10**9+7))