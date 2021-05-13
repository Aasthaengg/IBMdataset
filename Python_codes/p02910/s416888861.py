s=input()
t=0
if any([i=="R" for i in s[1::2]]) or any([i=="L" for i in s[::2]]):
    t=1
print("YNeos"[t::2])