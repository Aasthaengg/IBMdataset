A,B,K = map(int,input().split())
counter = 0
while True:
    if A%2 != 0:
        A -= 1
    A = A/2
    B += A
    counter += 1

    if counter == K:
        break
    if B%2 != 0:
        B -= 1
    B = B/2
    A += B
    counter += 1

    if counter == K:
        break

print(int(A),int(B))
