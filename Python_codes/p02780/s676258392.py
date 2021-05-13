n,k=map(int, input().split())
pn = list(map(int, input().split()))
ex_list = [(pn[i]+1)/2 for i in range(len(pn))]
ex_wa_list = []
wa = 0
for i in range(len(ex_list)):
    wa += ex_list[i]
    ex_wa_list.append(wa)
Ans_list = []
wa2 = 0
for i in range(n-k+1):
    if i == 0:
        wa2 = ex_wa_list[k-1]
    else:
        wa2 = ex_wa_list[k-1+i] - ex_wa_list[i-1]
    Ans_list.append(wa2)
print(max(Ans_list))