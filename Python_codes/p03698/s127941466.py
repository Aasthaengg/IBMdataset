#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


ans = [0] * 26

s = input()

for i in range(len(s)):
    idx = ord(s[i]) - 0x61
    ans[idx] += 1
    if (ans[idx] > 1):
        print("no")
        exit()
print("yes")


