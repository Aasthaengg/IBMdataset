from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
a_count = Counter(a)
cnt = 0
for key,value in a_count.items():
    if value % 2 == 1:
        cnt += 1
    else:
        pass
print(cnt)