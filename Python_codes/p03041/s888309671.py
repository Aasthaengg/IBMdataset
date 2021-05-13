n, k = map(int,input().split())
s = input()
l = s[k - 1]
if l == "A":
    x = s[:(k - 1)] + "a" + s[k:]
elif l == "B":
    x = s[:(k - 1)] + "b" + s[k:]
else:
    x = s[:(k - 1)] + "c" + s[k:]
print(x)