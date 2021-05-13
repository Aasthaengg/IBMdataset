S = input()
k = int(input())
for i, s in enumerate(S, start=1):
    if s != "1":
        print(s)
        break
    if i == k:
        print(1)
        break