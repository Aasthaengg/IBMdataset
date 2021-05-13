N = int(input())
A = list(map(int, input().split()))

num_minus = [a < 0 for a in A].count(True)

B = [abs(a) for a in A]

if num_minus%2 == 0:
    print(sum(B))
else:
    b = sorted(B)[0]
    print(sum(B) - 2*b)
