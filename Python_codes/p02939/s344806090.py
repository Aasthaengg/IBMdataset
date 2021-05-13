def calc(pr, s):
    cnt = 0
    i = 0
    while i < len(s)-1:
        if len(pr) == 1:
            if s[i+1] == pr:
                if i+2 < len(s):
                    cnt += 1
                    pr = s[i+1:i+3]
                    i += 1
                else:
                    break
            else:
                cnt += 1
                pr = s[i+1]
                i += 1
        else:
            if i+2 < len(s):
                cnt += 1
                pr = s[i+2]
                i += 2
            else:
                break
    return cnt+1

s = input()
pr1 = s[0]
pr2 = s[:2]
print(max(calc(pr1, s), calc(pr2, s)))