n = int(input())
s = input()
t = input()
for i in range(n):
    if t.startswith(s[i:]):
        print(i+n)
        break
else:
    print(n*2)