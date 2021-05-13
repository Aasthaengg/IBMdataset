def stones(k, moves):
    winnable = [False] * (k + 1)
    for i in range(1, k+1):
        winnable[i] = not all(winnable[i - j] for j in moves if j <= i)
    return ["Second", "First"][winnable[k]]

def main():
    n, k = [int(x) for x in input().split()]
    moves = [int(x) for x in input().split()]
    return stones(k, moves)

print(main())