s = input()
words = ["dreamer", "dream", "eraser", "erase"]
while len(s) > 0:
    match = [s.endswith(i) for i in words]
    if True in match:
        ans = words[match.index(True)]
        s = s[:-len(ans)]
        if len(s) == 0:
            print("YES")
            break
    
    else:
        print("NO")
        break