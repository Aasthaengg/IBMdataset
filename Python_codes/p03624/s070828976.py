s = input()
t = sorted(set(list(s)))
if len(set(s)) >= 26:
    print("None")
    exit()

alp = [chr(i) for i in range(97, 97+26)]
for i in alp:
    if i not in t:
        print(i)
        exit()