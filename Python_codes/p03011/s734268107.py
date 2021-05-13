PQR = list(map(int, input().split()))
PQR.remove(max(PQR))

print(sum(PQR))