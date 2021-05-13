n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = sum([1 for tmp_t in T if tmp_t in S])

print(ans)