S = input()
ans = [0]*len(S)
R = 0
L = 0
first = 0
count = 0
for i in range(len(S)-1):
    if S[i] == "L" and S[i+1] == "R":
        count += 1
        if count % 2 == 1:
            if (R - first) % 2 == 0:
                ans[R] = count//2 + 1
                ans[L] = count//2
            else:
                ans[R] = count//2 
                ans[L] = count//2 + 1
        else:
            ans[R] = count//2
            ans[L] = count//2
        count = 0
        R = 0
        L = 0
        first = -1
    elif S[i] == "R" and S[i+1] == "L":
        R = i
        L = i+1
        count += 1
    else:
        count += 1
    if first == -1:
        first = i+1
count += 1
if count % 2 == 1:
    if (R - first) % 2 == 0:
        ans[R] = count//2 + 1
        ans[L] = count//2
    else:
        ans[R] = count//2 
        ans[L] = count//2 + 1
else:
    ans[R] = count//2
    ans[L] = count//2
print(" ".join(map(str, ans)))