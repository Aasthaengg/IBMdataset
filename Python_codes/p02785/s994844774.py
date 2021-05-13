N, K = map(int, input().split())
H_list = list(map(int, input().split()))

H_list_min = sorted(H_list)
H_list_sum = 0

for i in range(len(H_list_min)-K):
    H_list_sum += H_list_min[i]

print(H_list_sum)