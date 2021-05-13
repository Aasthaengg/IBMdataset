A = list(map(int, input().split()))
maxa = max(A)
A.remove(maxa)
maxa2 = max(A)
cost = maxa - maxa2
A.remove(maxa2)
cost += maxa2 - A[0]
print(cost)