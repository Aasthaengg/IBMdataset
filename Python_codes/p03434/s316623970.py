n = int(input())
a = list(map(int, input().split()))
A = sorted(a, reverse = True)

ali = []
bob = []
for i in range(n):
    if i % 2 == 0:
        ali.append(A[i])
    else:
        bob.append(A[i])
        
print(sum(ali) - sum(bob))