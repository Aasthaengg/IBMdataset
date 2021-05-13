sl = list(input())
k = int(input())

for i in range(len(sl)):
    ord_s = ord(sl[i])
    use = 123 - ord_s
    if k - use >= 0 and sl[i] != "a":
        sl[i] = "a"
        k -= use

if k > 0:
    sl[-1] = chr((ord(sl[-1]) + k - 97) % 26 + 97)

print("".join(sl))

