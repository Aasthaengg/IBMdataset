s = list(input())

out = 0

if len(s) % 2 != 0:
    print("No")
else:
    for i in range(0, len(s), 2):
        if s[i] == 'h' and s[i+1] == 'i':
            continue
        else:
            out = 1

    if out:
        print("No")
    else:
        print("Yes")