N = input()
S = list(input())
count = 0
num_count = [False]*10
for i in range(len(S)-2):
    s_i = int(S[i])
    if num_count[s_i]:
        continue
    num_count[s_i] = True
    num_count_2 = [False]*10
    for j in range(i+1, len(S)-1):
        s_j = int(S[j])
        if num_count_2[s_j]:
            continue
        num_count_2[s_j] = True
        num_count_3 = [False] * 10
        for k in range(j+1, len(S)):
            s_k = int(S[k])
            if num_count_3[s_k]:
                continue
            num_count_3[s_k] = True
            count += 1
print(count)
