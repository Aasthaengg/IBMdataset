n = int(input())
s = input()
t = input()

for i in range(n+1):
    for j in range(n+1):
        tmp = s[:i] + t[:j]
        if tmp[:n] == s and tmp[-n:] == t:
            print(len(tmp))
            exit()
