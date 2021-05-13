K = int(input(""))
S = input("")
l = ""

if K < len(S):
    l += S[:K]
    print(l + "...")
else:
    print(S)
