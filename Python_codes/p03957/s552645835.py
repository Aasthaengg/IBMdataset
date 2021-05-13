def solve():
    s = input()
    bit = 0
    for i in range(len(s)):
        if bit == 0:
            if s[i] == "C":
                bit = 1
        if bit == 1:
            if s[i] == "F":
                bit = 2
                break
    if bit == 2:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == "__main__":
    solve()