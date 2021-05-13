def is_gu(s):
    if s[0:len(s)//2] == s[len(s)//2:len(s)]:
        return True
    return False

S = input()
ans = len(S)-2

while True:
    if is_gu(S[0:ans]):
        break
    else:
        ans = ans-2

print(ans)