N = int(input())
B = list(map(int, input().split()))
A = [B[0]] + [min(B[i], b) for i,b in enumerate(B[1:])] + [B[-1]]
print(sum(A))
