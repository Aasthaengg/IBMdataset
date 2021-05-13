N,K = map(int,input().split())
S = input()
one = [0]
zero = [0]
if S[0] == '0':
    one.append(0)
cnt = 1
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        if S[i-1] == '1':
            one.append(cnt+one[-1])                
        else:
            zero.append(cnt+zero[-1])                
        cnt = 1
    else:
        cnt += 1
else:
    if S[-1] == '1':
        one.append(cnt+one[-1])                
    else:
        zero.append(cnt+zero[-1])                
        one.append(one[-1])                
window_size = min(len(zero)-1,K)
MAX = 0
for i in range(len(zero)-window_size):
    if MAX < (zero[i+window_size] - zero[i]) + (one[i+window_size+1] - one[i]):
        MAX = (zero[i+window_size] - zero[i]) + (one[i+window_size+1] - one[i])

print(MAX)
