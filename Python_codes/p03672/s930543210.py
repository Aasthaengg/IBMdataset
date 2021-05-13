s = input()
l = [s[:-i] for i in range(1,len(s)-1)]

for i in range(len(l)):
    half = len(l[i])//2
    if len(l[i]) % 2 == 0:
        if l[i][:half] == l[i][half:]:
            print(len(l[i]))
            exit()
