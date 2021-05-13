from collections import defaultdict

N, M = map(int, input().split())
a_list = list(map(int, input().split()))

num_dict = defaultdict(int)
for a in a_list:
    num_dict[a] += 1
for _ in range(M):
    b, c = map(int, input().split())
    num_dict[c] += b

ans = 0
num_list = sorted(num_dict.items(), key=lambda x: x[0], reverse=True)

for num, cnt in num_list:
    for _ in range(cnt):
        ans += num
        N -= 1
        if N == 0:
            print(ans)
            exit()