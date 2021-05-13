N,A,B = map(int,input().split())
print(min(A,B),0 if min(A,B)-N+max(A,B) < 0 else min(A,B)-N+max(A,B))