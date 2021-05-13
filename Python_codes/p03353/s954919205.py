s = input()
k = int(input())

sl = [s]
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if j - i > k:
            break
        ss = s[i:j]
        sl.append(ss)
sl = sorted(list(set(sl)))
print(sl[k-1])