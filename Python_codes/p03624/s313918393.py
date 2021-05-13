S=input()

alphabet="abcdefghijklmnopqrstuvwxyz"

ans = "None"

for i in range(len(alphabet)):
    if alphabet[i] in S:
        continue
    else:
        ans = alphabet[i]
        break
print(ans)