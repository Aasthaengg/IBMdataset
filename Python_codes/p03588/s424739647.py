N=int(input())
print(sum(max(tuple(map(int, input().split()))for _ in range(N))))