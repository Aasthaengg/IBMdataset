n = input()

sum = int(n[0]) + (len(n)-1) * 9

if len(n) == 1:
    print(n)
else:
    print(sum if set(n[1:]) == {"9"} else sum - 1)
