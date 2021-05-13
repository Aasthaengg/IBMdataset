N = int(input())
S = input()
k = 1
ans_list = []
for i in range(1000,2000):
    ansyo = str(i)
    for j in range(0,N):
        if ansyo[k] == S[j]:
            k += 1
        if k == 4:
            ans_list.append(ansyo)
            k = 1
        if j == N-1:
            k = 1
ans_list = set(ans_list)
print(len(ans_list))