S = input()
is_true = True
for i in range(len(S)):
    if S.count(S[i]) != 2:
        is_true =  False
        break
if is_true:
    print("Yes")
else:
    print("No")