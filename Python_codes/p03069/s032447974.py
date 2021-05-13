N = int(raw_input())
S = raw_input()

count_white = [0]*N

for i in range(N):
    if S[i] == ".":
        count_white[i] = count_white[i-1] + 1
    else:
        count_white[i] = count_white[i-1]

white_total = count_white[-1]
ans = 10**9
for i in range(N):
    num_black_left = i+1 - count_white[i]
    num_white_right = white_total - count_white[i]

    ans_temp = num_black_left + num_white_right

#    print i, ans_temp                                                                                                                                    

    ans = min(ans, ans_temp)

print min(ans, white_total)


