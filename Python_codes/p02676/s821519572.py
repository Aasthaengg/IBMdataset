k = int(input())
s = input()

if k >= len(s):
    print(s)
elif k <= len(s):
    print(s[0: k] + "...")