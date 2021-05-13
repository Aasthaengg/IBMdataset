n = int(input())
s = []
r = []
sr = []
for i in range(n):
    s, r = map(str, input().split())
    sr.append([i+1, s, int(r)])
# print(sr)
sr1 = sorted(sr, key=lambda x:x[2], reverse=True)

ans = sorted(sr1, key=lambda x:x[1])

for i in range(n):
    print(ans[i][0])