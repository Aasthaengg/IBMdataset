N, M, X = map(int, input().split())
A = list(map(int, input().split()))

print(min(len([x for x in A if x<X]), len([x for x in A if x>X])))