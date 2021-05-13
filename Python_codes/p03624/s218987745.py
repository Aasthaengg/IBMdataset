T = input()
L = [chr(l) for l in range(ord("a"), ord("z")+1)]
L = [l for l in L if l not in T]
print(min(L) if len(L)>0 else "None")
