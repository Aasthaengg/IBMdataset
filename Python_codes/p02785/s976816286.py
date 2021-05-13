N,K = map(int,input().split())
HP = list(map(int,input().split()))
HP.sort(reverse=True)
ans = 0
ans += sum(HP[K:])
print(ans)