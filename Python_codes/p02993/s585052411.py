s = input()
s_prev = ""
for s_i in s:
    if s_i == s_prev:
        print('Bad')
        exit()
    s_prev = s_i
print('Good')