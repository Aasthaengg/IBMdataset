S_len = int(input().rstrip())
S = input().rstrip().split(" ")
T_len = int(input().rstrip())
T = input().rstrip().split(" ")

cnt = 0
for t in T:
    cnt += t in S
print(cnt)

