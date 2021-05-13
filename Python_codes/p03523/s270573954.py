s = input()
n = len(s)
if s.count("A") <= 4 and s.replace("A", "") == "KIHBR":
    for i in range(1, n):
        if s[i] == "A" and s[i - 1] not in ["H", "B", "R"]: 
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")