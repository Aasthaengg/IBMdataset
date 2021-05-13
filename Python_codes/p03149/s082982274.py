N = set(int(i) for i in input().split())

if len(N) == 4 and set([1,9,7,4]) == N:
    print("YES")
else:
    print("NO")