S = input()
is_good = True
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        is_good = False
if is_good:
    print("Good")
else:
    print("Bad")