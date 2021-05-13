n = int(input())
frames = list(map(int, input().split()))

sum = 0
for i in frames:
    sum += i

mean = sum/len(frames)

diff_lists = []
for j in frames:
    diff = j - mean
    diff_lists.append(abs(diff))

tmp_lists = diff_lists.copy()
tmp_lists.sort()
ans = diff_lists.index(tmp_lists[0])

print(ans)