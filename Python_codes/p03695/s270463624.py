N = int(input())
S = list(map(int,input().split()))

col_list = [399,799,1199,1599,1999,2399,2799,3199]
count_list = [0]*(len(col_list)+1)

for i in range(N):
    for j in range(len(col_list)+1):
        if j == len(col_list):
            if 3200<=S[i]:
                count_list[j] = count_list[j] + 1
        elif S[i]<=col_list[j]:
            count_list[j] = count_list[j]+1
            break

ans = 0
for i in range(len(col_list)):

    if count_list[i] != 0:
        ans += 1
print(str(max(ans,1)) + ' ' + str(ans+count_list[-1]))

