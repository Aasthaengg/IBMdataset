N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

total = 0
for a in A_list:
    total += B_list[a-1]

for i in range(N-1):
    if A_list[i] + 1 == A_list[i + 1]:
        total += C_list[A_list[i]-1]

print(total)