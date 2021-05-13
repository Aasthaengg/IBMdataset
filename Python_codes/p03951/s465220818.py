n = int(input())
s = input()
t = input()
for i in range(n - 1, -1, -1):
    if s[-i-1:] == t[:i + 1]:
        print(n * 2 - i - 1)
        break
else:
    print(n * 2)