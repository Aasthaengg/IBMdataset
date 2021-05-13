s = input()
t = input()

sl = list(s)
sl.sort()
tl = list(t)
tl.sort()
tl=tl[::-1]
S="".join(sl)
T="".join(tl)
if S<T:
    ans ='Yes'
else:
    ans = 'No'
print(ans)