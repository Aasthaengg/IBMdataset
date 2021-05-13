N, *S = map(int, open(0).read().split())

B = [s for s in S if s % 10]

if len(B) == 0:
    print(0)
elif len(B) % 2 == 0:
    print(sum(S) - min(B))
else:
    if sum(S) % 10:
        print(sum(S))
    else:
        print(sum(S) - min(S))