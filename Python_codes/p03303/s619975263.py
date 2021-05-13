l = []
l += input()
n = int(input())
ans = []
for i in range((len(l) - 1) // n + 1):
    ans += l[i*n]
print("".join(ans))