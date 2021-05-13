K, S = map(int, input().split())
print(sum(S - K <= X + Y <= S for X in range(K + 1) for Y in range(K + 1)))