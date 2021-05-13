s,t = input().split()

cnt = {}
cnt[s], cnt[t] = map(int, input().split())
u = input()
cnt[u]-=1

print(cnt[s], cnt[t])
