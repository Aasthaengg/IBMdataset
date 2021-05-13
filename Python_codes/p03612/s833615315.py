n = int(input())
p_ls = list(map(int, input().split()))
same_ls = [0] * n

for i in range(n):
    if p_ls[i] == i+1:
        same_ls[i] = 1
count = 0
for i in range(n-1):
    if same_ls[i] == 1:
        same_ls[i+1] = 0
        count += 1
if same_ls[n-1] == 1:
    count += 1
print(count)



