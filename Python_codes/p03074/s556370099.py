N, K  = map(int, input().split())
S = input()

lst = [0]
for i in range(N - 1):
    if S[i] != S[i + 1]:
        lst.append(i + 1)
lst.append(N)
# print(lst)

sub = []
for j in range(1, len(lst)):
    sub.append(S[lst[j - 1]:lst[j]])
# print(sub)
diff = [lst[i + 1] -lst[i] for i in range(len(lst) - 1)]
# print(diff)

if S[0] == '1' and len(lst) - 1 <= 2 * K + 1:
    print(N)
elif S[0] == '0' and len(lst) - 1 <= 2 * K:
    print(N)
else:
    candicate = []
    for i in range(len(lst) - 1 - K * 2):
        if S[lst[i]] == '1':
            candicate.append(lst[i + K * 2 + 1] - lst[i])
    if S[-1] == '0':
        candicate.append(lst[-1] - lst[-1 - K * 2])
    for i in range(len(lst) - K * 2):
        if S[lst[i]] == '0':
            candicate.append(lst[i + K * 2] - lst[i])
    # print(candicate)
    print(max(candicate))



