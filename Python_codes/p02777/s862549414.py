s, t = map(str, input().split())
a, b = map(int, input().split())

query = input()
if query == s:
    a -= 1
else:
    b -= 1
print(str(a) + " " + str(b))