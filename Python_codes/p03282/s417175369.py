s = input().rstrip()
n = int(input().rstrip())

if s[:n].count('1') == n:
    print(1)
else:
    print(s.replace('1', '')[0])