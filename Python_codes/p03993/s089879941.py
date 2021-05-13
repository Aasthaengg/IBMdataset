N = int(input())
A_list = list(map(int, input().split()))

cnt = 0
for i, ai in enumerate(A_list):
    if i < ai:
        if (A_list[ai-1] - 1) == i:
            cnt += 1
print(cnt)            
