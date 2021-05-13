#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

s = input()
n = len(s)
def func(s):
    if s == "A" or s == "C" or s == "G" or s == "T":
        return True
    else:
        return False

ans = 0
for i in range(n):
    le = 0
    if func(s[i]):
        le = 1
        for j in range(i+1,n):
            if func(s[j]):
                le += 1
            else:
                break
    ans = max(ans, le)
print(ans)



