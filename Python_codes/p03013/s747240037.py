N,M = list(map(int,input().split()))
a = [int(input()) for i in range(M)]
a_complement = list((set(list(range(N+1))) ^ set(a)))
cnt = {s: 0 for s in range(-2,N+1)}
cnt[0] = 1

for i in a_complement:
  cnt[i] += cnt[i-1] + cnt[i-2]

print(cnt[N] % 1000000007)