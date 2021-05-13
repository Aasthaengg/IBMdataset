N = input()
len_N = len(N)

if N[1:] == '9' * (len_N - 1):
    tmp = int(N[0]) + (len_N - 1) * 9
else:
    tmp = int(N[0]) + (len_N - 1) * 9 - 1
print(tmp)