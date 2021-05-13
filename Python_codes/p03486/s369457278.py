s = list(input().rstrip())
t = list(input().rstrip())

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
for i in range(len(s)):
    s[i] = alphabet.index(s[i])
for i in range(len(t)):
    t[i] = alphabet.index(t[i])
s.sort()
t.sort()
t.reverse()
flg = "Yes"
check = 0
for j in range(min(len(s),len(t))):
    if t[j] > s[j]:
        check = 1
        break
    elif t[j] < s[j]:
        flg = "No"
        check = 1
        break
if check == 0:
    if len(s) >= len(t):
        flg = "No"
print(flg)