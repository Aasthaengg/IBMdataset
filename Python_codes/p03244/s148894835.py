import collections

N = int(input())
A = list(map(int,input().split()))
odd = []
even = []
for i in range(N):
    if i % 2 == 1:
        odd.append(A[i])
    else:
        even.append(A[i])
Dic_odd = collections.Counter(odd)
Dic_eve = collections.Counter(even)
M_odd = Dic_odd.most_common()
M_eve = Dic_eve.most_common()
#print(M_odd, M_eve)
if M_odd[0][0] != M_eve[0][0]:
    ans = len(odd) - M_odd[0][1] + len(even) - M_eve[0][1]
else:
    if len(M_odd) == 1 and len(M_eve) == 1:
        ans = min(len(odd), len(even))
    elif len(M_odd) == 1:
        ans = min(len(even) - M_eve[1][1], len(even) - M_eve[0][1] + len(odd))
    elif len(M_eve) == 1:
        ans = min(len(odd) - M_odd[1][1], len(odd) - M_odd[0][1] + len(even))
    else:
        ans = len(odd) + len(even) - max(M_odd[0][1] + M_eve[1][1], M_odd[1][1] + M_eve[0][1])
print(ans)