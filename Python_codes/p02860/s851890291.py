n = int(input())
s = input()

if len(s)%2 != 0:
    print("No")
else:
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")
