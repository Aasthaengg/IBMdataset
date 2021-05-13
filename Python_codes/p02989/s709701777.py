N = int(input())
difficulty = list(map(int, input().split()))
difficulty.sort()

print(difficulty[int(N/2)] - difficulty[int(N/2)-1])