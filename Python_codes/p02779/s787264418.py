N = input()
A = list(map(int, input().split()))

print(['YES', 'NO'][len(A) != len(set(A))])