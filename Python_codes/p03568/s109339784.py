N = int(input())
A = list(map(int, input().split()))
combiIncludingOdd = 3**len(A)

c = 1
for a in A:
    if a % 2 == 0:
        c*=2
print(combiIncludingOdd-c)