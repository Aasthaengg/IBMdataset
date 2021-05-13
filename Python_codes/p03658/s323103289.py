N , K = map(int,input().split())
A = list(map(int,input().split()))

rev_sorted_A = list(reversed(sorted(A)))
print(sum(rev_sorted_A[:K]))