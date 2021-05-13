S = sorted(list(set(input())))
ABC = [chr(i) for i in range(97, 123)]
S_box = ["F" for i in range(26)]
ans = "None"
for i in range(26):
    for j in range(len(S)):
        if S[j] == ABC[i]:
            S_box[i] = ABC[i]
if len(S) == 26:
    pass
else:
    for i in range(26):
        if S_box[i] == "F":
            ans = ABC[i]
            break            
print(ans)