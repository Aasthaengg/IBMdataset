s = input()
t = input()
anas = sorted(s)
at = sorted(t,reverse = True)

miji = min(len(s),len(t))
for i in range(miji):
    if ord(anas[i]) < ord(at[i]):
        print('Yes')
        exit()
    elif ord(anas[i]) > ord(at[i]):
        print('No')
        exit()

if len(s) < len(t):
    print('Yes')
else:
    print('No')


