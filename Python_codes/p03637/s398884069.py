N = int(input())
A_s = list(map(int, input().split()))

N_list = [0] * 3

for i in range(N):
    num = A_s[i]
    
    if (num % 4 == 0):
        N_list[2] += 1
    elif (num % 2 == 0):
        N_list[1] += 1
    else:
        N_list[0] += 1

if (N_list[2] >= N_list[0]):
    ans = 'Yes'
elif (N_list[1] == 0 and N_list[2] + 1 == N_list[0]):
    ans = 'Yes'
else:
    ans = 'No'

print(ans)