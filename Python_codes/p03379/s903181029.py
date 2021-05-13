n = int(input())
X = list(map(int, input().split()))
sort_x = sorted(X)

smaller = sort_x[n//2-1]
bigger = sort_x[n//2]

for x in X:
    if x <= smaller:
        print(bigger)
    else:
        print(smaller)