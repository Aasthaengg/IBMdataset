import copy
N = int(input())
A = list(map(int, input().split()))
K = [0]*21
bin_num = format(A[0], 'b')
bin_num = bin_num[::-1]
for i in range(len(bin_num)):
    if bin_num[i] == "1":
        K[i] = 1
start = 0
end = 0
ans = 0
while(True):
    if start == N:
        break
    t = 0
    for j in range(end+1, N):
        K_ex = K.copy()
        bin_num = format(A[j], 'b')
        bin_num = bin_num[::-1]
        for l in range(len(bin_num)):
            if bin_num[l] == "1" and K[l] == 1:
                t = 1
            if bin_num[l] == "1":
                K[l] = 1
        if t == 1:
            K = K_ex.copy()
            bin_num = format(A[start], 'b')
            bin_num = bin_num[::-1]
            for p in range(len(bin_num)):
                if bin_num[p] == "1":
                    K[p] = 0
            end = j - 1
            break
    if t == 0:
        end = N - 1
    ans += end - start + 1
    start += 1
print(ans)