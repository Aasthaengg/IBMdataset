N = int(input())
A, B = map(int, input().split())
p = list(map(int, input().split()))
c1, c2, c3 = 0, 0, 0

for pi in p:
    if pi<=A:
        c1 += 1
    elif A<pi<=B:
        c2 += 1
    else:
        c3 += 1

print(min(c1, c2, c3))