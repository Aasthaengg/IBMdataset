import copy
s = input()

alpha_list = "abcdefghijklmnopqrstuvwxyz"

ans = 10**4
for alpha in alpha_list:
#    print(alpha)
    s_check = copy.deepcopy(s)

    mojisu_count = 0
    for i in range(len(s_check)):
        if(len(s_check) == s_check.count(alpha)):
            ans = min(ans, mojisu_count)
            break

        s_dash = ""
        for j in range(len(s_check) - 1):
            if(s_check[j] == alpha or s_check[j+1] == alpha):
                s_dash += alpha
            else:
                s_dash += s[j]

        mojisu_count += 1
        s_check = copy.deepcopy(s_dash)

print(ans)