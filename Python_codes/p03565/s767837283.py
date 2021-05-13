S = input()
T = input()

partial_s = []
for i in range(len(S)-len(T)+1):
    partial_s.append(S[i:i+len(T)])
to_replace_idxs = []

for idx, sub_s in enumerate(partial_s):
    for i in range(len(sub_s)):
        flag = 1
        if sub_s[i] != T[i]:
            if sub_s[i] != "?":
                flag = 0
                break
    if flag:
        to_replace_idxs.append(idx)

tmp_ans = []
if not to_replace_idxs:
    print("UNRESTORABLE")
else:
    for to_replace_idx in to_replace_idxs:
        tmp_string = S
        tmp_string = list(tmp_string)
        for i in range(to_replace_idx, to_replace_idx+len(T)):
            tmp_string[i] = T[i-to_replace_idx]
            
        tmp_string = "".join(tmp_string)
        tmp_string = tmp_string.replace("?", "a")
        tmp_ans.append(tmp_string)
    print(min(tmp_ans))