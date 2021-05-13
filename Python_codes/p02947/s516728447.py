from collections import Counter
N=int(input())

alpha2num = lambda c: ord(c) - ord('a')

S_num_list=[]

for n in range(N):
    S_=input()
    S_num=[0]*26
    for s in S_:
        S_num[alpha2num(s)] += 1
    S_num_list.append(''.join(map(str,S_num)))
    
S_counter=Counter(S_num_list)

ans=0
for s in S_counter.keys():
    s_num = S_counter[s]
    s_combination_num = int((s_num*(s_num-1))/2)
    ans += s_combination_num
print(ans)