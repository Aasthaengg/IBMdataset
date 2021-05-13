import bisect

N,M = list(map(int, input().split()))
As = list(map(int, input().split()))

As.sort()

#print(As)

for _ in range(M):
    discount = As.pop(-1)

    if(discount == 0):
        break

    discount //= 2

    i = bisect.bisect_left(As, discount)
    As.insert(i, discount)
#    print(As)

print(sum(As))