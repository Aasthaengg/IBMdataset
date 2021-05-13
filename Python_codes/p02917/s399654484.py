import copy

N = int(input())
Bs = list(map(int, input().split()))

As = [copy.copy(Bs[0])]
As.extend(copy.copy(Bs))

#print(Bs)
#print(As)

for index, B in enumerate(Bs):
#    print(Bs)
#    print(As)
    if B < As[index]:
        As[index] = B

#print(As)
print(sum(As))

