import sys

input = sys.stdin.readline
S =  input()
S = S.replace("\n","")
s_list = list(S)
alpha_list = [chr(i) for i in range(97, 97+26)]
flag_list = [False for _ in range(26)]


if len(s_list) == 26:
    for i in range(25, 0, -1):
        if s_list[i - 1] < s_list[i]:
            c = 'ω'
            for j in range(i, 26):
                if s_list[i - 1] < s_list[j]:
                    c = min(c, s_list[j])
            print(S[:i-1] + c)
            exit(0)
    print(-1)

else:
    for i,alpha in enumerate(alpha_list):
        if alpha in s_list:
            flag_list[i] = True
    for i,flag in enumerate(flag_list):
        if not flag:
            print(S + alpha_list[i])
            break