s_prime = input()
t = input()
s_length = len(s_prime)
t_length = len(t)
t_start = -1 # tが入る最初のindex
for i in range(s_length-t_length+1):
    for j in range(t_length):
        flag = True
        # print(i, j, s_prime[i+j], t[j])
        if s_prime[i+j] == '?' or s_prime[i+j] == t[j]:
            pass
        else:
            flag = False
            break
    if flag:
        t_start = i

if t_start == -1:
    print('UNRESTORABLE')
    exit()
s = []
i = 0
while i < s_length:
    if i == t_start:
        s.append(t)
        i += t_length
    elif s_prime[i] == '?':
        s.append('a')
        i += 1
    else:
        s.append(s_prime[i])
        i += 1
for i in range(len(s)):
    print(s[i], end='')
print()
