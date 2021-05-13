o = input()
e = input()
print(*(e[i//2] if i%2 else o[i//2] for i in range(len(o+e))),sep='')