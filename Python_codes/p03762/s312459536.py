def make_list(a):
    t = a-1
    s = a-3
    anslist = [t]
    while s > 0:
        anslist.append(s+t)
        t += s
        s -= 2
    if a % 2 == 1:
        anslist += anslist[::-1]
    else:
        anslist = anslist[:-1] + anslist[::-1]
    return anslist

mod = 10**9+7
h, w = [ int(v) for v in input().split() ]
h_list = [ int(v) for v in input().split() ]
w_list = [ int(v) for v in input().split() ]
h_list_2 = [(h_list[i+1] - h_list[i]) % mod for i in range(h-1)]
w_list_2 = [(w_list[i+1] - w_list[i]) % mod for i in range(w-1)]
h_list_3 = make_list(h)
w_list_3 = make_list(w)
h_total = sum([(h_list_3[i] * h_list_2[i]) % mod for i in range(h-1)]) % mod
w_total = sum([(w_list_3[i] * w_list_2[i]) % mod for i in range(w-1)]) % mod

print((h_total*w_total)%mod)