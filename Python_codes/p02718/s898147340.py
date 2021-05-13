N,M = map(int, input().split())
A = list(map(int, input().split()))

print('No' if sorted(A)[-M]*M*4 < sum(A) else 'Yes')