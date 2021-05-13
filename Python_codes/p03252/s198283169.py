S = list(input())
T = list(input())

direct_graph1 = {}
direct_graph2 = {}
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
for i in list(ascii_lowercase):
    direct_graph1[i] = None
    direct_graph2[i] = None

flg = 0
for s,t in zip(S,T):
    if direct_graph1[s] == None or direct_graph1[s] == t:
        direct_graph1[s] = t
    else:
        flg =1
    
    if direct_graph2[t] == None or direct_graph2[t] == s:
        direct_graph2[t] = s
    else:
        flg = 1

    if flg == 1:
        print('No')
        exit()

print('Yes')