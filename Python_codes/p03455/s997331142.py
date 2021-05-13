s = input().rstrip().split(' ')
result = int(s[0]) * int(s[1]);

if (result % 2) != 0:
    print("Odd")
else:
    print("Even")
