N = int(input())
A = list(map(int,input().split()))

print(['NO','YES'][len(A)==len(set(A))])