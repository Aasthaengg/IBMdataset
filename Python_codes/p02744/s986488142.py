import itertools

n = int(input())
alpha = "abcdefghij"
ans_s = {}
if n == 1:
    print("a")
    exit()

def ans_string(max_num, num, ans):
    if num == 0:
        ans_s[ans] = 1
    else:
        for i in range(max_num + 2):
            ans_string(max(i, max_num), num - 1, ans + alpha[i])
        
ans_string(0, n - 1, "a")
for key, value in ans_s.items():
    print(key)