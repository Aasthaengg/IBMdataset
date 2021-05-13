N = int(input())
S = input()
res = ""
for x in S:
    res += chr((ord(x) - ord("A") + N)%26 + ord("A"))
print(res)