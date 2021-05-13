s = raw_input()
n = int(raw_input())
for i in range(n):
    tmp = raw_input().split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    if tmp[0] == "replace":
        s = s[:tmp[1]] + tmp[3] + s[tmp[2]+1:]
    elif tmp[0] == "reverse":
        s = s[:tmp[1]] + s[tmp[2]:tmp[1]:-1] + s[tmp[1]] + s[tmp[2]+1:]
    else:
        print s[tmp[1]:tmp[2]+1]
