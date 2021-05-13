def rotate(string):
    return string[-1] + string[0:-1]


S = input()
T = input()
ans = "No"
for i in range(len(S)):
    T = rotate(T)
    if S == T:
        ans = "Yes"
        break
print(ans)
