from collections import deque
S=input()
Q=int(input())

ct=0
reverse=[]
string=[deque(''), deque('')]
# 先頭に付け足す->string[0]にappendleft
# 最後尾に付け足す->strint[1]にappend
# ctの偶奇が変わる毎に付け足す方を変える

for i in range(Q):
    l=list(input().split())
    if l==['1']:
        reverse.append(i)
        ct+=1
    elif (int(l[1])+ct)%2==1:
        string[0].appendleft(l[2])
    else:
        string[1].append(l[2])

# print(string)
# print(ct)
if ct%2==0:
    top=''.join(string[0])
    bottom=''.join(string[1])
else:
    top=''.join(reversed(string[1]))
    bottom=''.join(reversed(string[0]))
    S=S[::-1]
    # print(S)
print(top+S+bottom)