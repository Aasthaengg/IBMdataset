#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

s = input()
ans = "Yes"
for i in range(len(s)):
    if ((i+1) % 2 == 1):
        if (s[i] != "R" and s[i] != "U" and s[i] != "D"):
            ans = "No"
            break
    else:
        if (s[i] != "L" and s[i] != "U" and s[i] != "D"):
            ans = "No"
            break
print(ans)


