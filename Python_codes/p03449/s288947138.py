n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
mx = 0
for idx in range(n) :
    list = a1[:idx+1] + a2[idx:]
    mx = max(mx, sum(list))
print(mx)
