N = int(input())
K = len(str(N))
c = N // 10**(K-1)

print(c+9*(K-1) if N ==(c+1)*10**(K-1)-1 else c+9*(K-1)-1)