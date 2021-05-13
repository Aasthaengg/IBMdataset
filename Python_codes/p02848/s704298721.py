#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

n = int(input())
s = input()

for i in range(len(s)):
    temp = ord(s[i]) + n
    if (temp > 90):
        temp = 64 + (temp - 90)
    print(chr(temp), end="")

