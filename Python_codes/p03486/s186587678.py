s = input()
t = input()
s = ''.join(sorted(s))
t = ''.join(sorted(t, reverse=True))
if s>=t:
    print('No' , flush=True)
else:
    print('Yes' , flush=True)
