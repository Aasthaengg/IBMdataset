N = int(input())
As = list(map(int, input().split()))

ans = 1/sum([1/A for A in As])
print(ans)
