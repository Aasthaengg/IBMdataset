N = int(input())

A_list = list(map(int, input().split()))

ans_list = [0 for i in range(N)]

for i in range(N-1):
    ans_list[A_list[i]-1] += 1

print(*ans_list, sep='\n')
