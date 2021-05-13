A,B,K = map(int, input().split())

D = [x for x in range(1, min(A,B)+1) if A%x == 0 and B%x == 0]

print(D[-K])