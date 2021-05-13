string = input()
k = int(input())
ans = list(string)

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_to_num = {}
for i in range(26):
    alpha_to_num[alpha[i]] = i
    
for i, s in enumerate(ans):
    if s == "a":
        continue
    pos = alpha_to_num[s]
    kk = 26 - pos
    if kk > k:
        continue
    k -= kk
    ans[i] = "a"
    
pos = alpha_to_num[ans[-1]]
new_pos = (k + pos) % 26
ans[-1] = alpha[new_pos]
print("".join(ans))