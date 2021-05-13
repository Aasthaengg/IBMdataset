import sys
input = sys.stdin.readline

N = int(input())
schedule = []
for i in range(N):
    A, B = map(int, input().split())
    schedule.append((A, B))

schedule = sorted(schedule, key=lambda x: x[1])
ans = 0
end = 0

flg = True
for i in range(N):
    end += schedule[i][0]
    if end <= schedule[i][1]:                   # 重複がダメならば等号を消す
         continue
    flg = False

print("Yes" if flg else "No")