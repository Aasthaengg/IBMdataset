s = list(input())
t = list(input())
cnt = 0
for i in range(len(s)):
    x = t[-1]
    t.pop()
    t.insert(0, x)
    if s == t:
        print("Yes")
        break
    else:
        cnt += 1
        if cnt == len(s):
            print("No")
            break