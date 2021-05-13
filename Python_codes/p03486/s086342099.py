s = input()
t = input()

ss = sorted(s)
tt = sorted(t, reverse=True)

print('Yes') if ss < tt else print('No')