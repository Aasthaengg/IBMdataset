A = [1, 9, 7, 4]
N = list(map(int, input().split()))
print("YES") if set(A) == set(N) else print("NO")
