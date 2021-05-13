N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
B = [{"id": i + 1, "order": A[i]} for i in range(len(A))]

B.sort(key=lambda b: b["order"])

print(" ".join([str(b["id"]) for b in B]))