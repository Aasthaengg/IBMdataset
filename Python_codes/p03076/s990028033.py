L = [int(input()) for _ in range(5)]
M = [(10-i%10)%10 for i in L]

print(sum(L)+sum(M)-max(M))
