N = int(input())
ans_list = ["a"]  # 生成元の初期状態 (N = 1 の答え)
alphabet = [chr(ord("a") + i) for i in range(N)]  # 使用するアルファベット

for i in range(N - 1):
    ans_list = [ans + x for ans in ans_list for x in alphabet[:len(set(ans)) + 1]]

for ans in ans_list:
    print(ans)