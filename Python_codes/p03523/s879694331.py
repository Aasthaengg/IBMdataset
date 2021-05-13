s = input()
akiba = 'AKIHABARA'
s_i = 0
aki_i = 0
while (s_i < len(s)) & (aki_i < len(akiba)):
    if s[s_i] == akiba[aki_i]:
        s_i += 1
        aki_i += 1
    else:
        if akiba[aki_i] == "A":
            aki_i += 1
        else:
            print("NO")
            exit()
if ((s_i == len(s)) & (aki_i >= 8)):
    print("YES")
else:
    print("NO")