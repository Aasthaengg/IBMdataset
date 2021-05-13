H, N = map(int, input().split())
N_list = list(map(int, input().split()))

for i in range(0, N):
    H -= N_list[i]

if H <= 0:
    print('Yes')
else:
    print('No')