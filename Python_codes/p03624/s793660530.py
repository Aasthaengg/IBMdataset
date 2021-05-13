s = list(sorted(set(input())))
lst = [chr(i) for i in range(97, 97+26)]

for i in lst:
    if not(i in s):
        print(i)
        exit()
else:
    print("None")