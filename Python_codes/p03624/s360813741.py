S = list(input())
a = [chr(i) for i in range(97, 97 + 26)]

for a in a:
    if S.count(a) == 0:
        print(a)
        break
else:
    print(None)