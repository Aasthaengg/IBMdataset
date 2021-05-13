N = int(input())
P = [int(input()) for _ in range(N)]

longest_increasing_subsequence = [0]*(N+1) #[i]: i以下の数字による最長増加部分文字列

for p in P:
  longest_increasing_subsequence[p] = max(1, longest_increasing_subsequence[p-1]+1)

#print(longest_increasing_subsequence)
print(N - max(longest_increasing_subsequence))
