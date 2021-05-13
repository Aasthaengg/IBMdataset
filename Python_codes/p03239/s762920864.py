N, T = input().split()
all_list = []
for i in range(int(N)):
    for j in input().split():
        all_list.append(int(j))

all_pattern_list = sorted(list(zip(*[iter(all_list)]*2)))

for pattern in all_pattern_list:
    if pattern[1] <= int(T):
        print(pattern[0])
        break
    elif pattern == all_pattern_list[-1]:
        print('TLE')