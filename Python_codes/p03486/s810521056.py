s = str(input())
t = str(input())

s_ = list(s)
s_.sort()
s_ = ''.join(s_)

t_ = list(t)
t_.sort(reverse= True)
t_ = ''.join(t_)

if s_ == t_:
    print('No')
    exit()

L = [(s_, 0), (t_, 1)]
L.sort()
#print(L)
if L[0][1] == 0:
    print('Yes')
else:
    print('No')
