N = int(input())
s = [int(input()) for _ in range(N)]
s.sort()
sums = sum(s)

if sums % 10 != 0:
    print(sums)
else:
    for p in s:
        if p % 10 != 0:
            print(sums - p)
            break
    else:
        print(0)