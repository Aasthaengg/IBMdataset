
def check(s: str) -> bool:
    ls = len(s)
    if ls % 2 != 0:
        return False
    else:
        if "".join(s[:ls//2]) == "".join(s[ls//2:]):
            return True


s = input()
l = len(s)
ans = 0
for i in reversed(range(l-1)):
    if check(s[0:i + 1]):
        ans = i+1
        break

print(ans)
