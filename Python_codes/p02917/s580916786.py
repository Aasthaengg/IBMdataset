N = int(input())
B = [int(x) for x in input().split()]
res = B[0] + B[-1]

for i in range(len(B) - 1):
    res += min(B[i], B[i+1])

print(res)