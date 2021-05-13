N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

diff_list = []
for h in H:
    diff = abs(A - (T - h * 0.006))
    diff_list.append(diff)

print(diff_list.index(min(diff_list)) + 1)