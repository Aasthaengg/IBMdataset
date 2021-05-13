# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_b

n = int(input())
i = 1
ans = []
while i * (i + 1) // 2 <= n:
    ans.append(i)
    i += 1
else:
    ans.append(i)
s = i * (i + 1) // 2
diff = s - n

if diff > 0:
    ans.remove(diff)
print(*ans, sep='\n')