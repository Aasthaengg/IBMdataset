s = input()
t = input()

if len(t) > len(s):
    print("UNRESTORABLE")
    exit()

s = s[::-1]
t = t[::-1]
for i in range(len(s)-len(t)+1):
    k = 0
    while True:
        if k == len(t):
            ans = s[:i] + t + s[i+len(t):]
            print(ans[::-1].replace("?","a",len(ans)))
            exit()
        if t[k] == s[i+k] or s[i+k] == "?":
            k += 1
        else:
            break
print("UNRESTORABLE")