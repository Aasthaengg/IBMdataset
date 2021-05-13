a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
cnt = [0,0,0,0]
cnt[a1-1] += 1
cnt[a2-1] += 1
cnt[a3-1] += 1
cnt[b1-1] += 1
cnt[b2-1] += 1
cnt[b3-1] += 1
print("YES" if max(cnt) < 3 else "NO")