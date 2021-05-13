A,B,C = list(map(int, input().split()))

res = B//A

if res >= C:
    print(C)
else:
    print(res)