N = int(input())
S, T = input().split(" ")
res = ""

for i, j in zip(S, T):
    res = res + i + j

print(res)