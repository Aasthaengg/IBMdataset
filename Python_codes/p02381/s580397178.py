import math
while True:
    n = int(input())
    if n == 0:
        break
    li = list(map(int, input().split()))
    avg = sum(li)/n
    S = sum([(li[i]-avg)**2 for i in range(n)]) / n
    print(f"{math.sqrt(S):0.9f}")

