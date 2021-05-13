n = "keyence"
s = input()

for i in s:
    if n[0] == i: #文字が一致するなら
        n = n[1:] #比較中の文字を削る
    else:
        break

n = n[::-1]

for i in s[::-1]:
    if n == "":
        break
    elif n[0] == i:
        n = n[1:]
    else:
        break

if n == "":
    print("YES")
else:
    print("NO")