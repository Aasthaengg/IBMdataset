s = input()
l = list(s)
sum_ = 0
for i in range(1 << len(l) -1):
    ll = []
    for j in range(len(l)):
#         print(i,j)
        ll +=[l[j]]
        if i & (1 << j):
            ll +=['+']
#     print(''.join(ll))    
    sum_ += eval(''.join(ll))
print(sum_)