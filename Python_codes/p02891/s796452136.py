import sys
s = input()
k = int(input())
data = []
start = s[0]
seq = 1
if len(set(list(s))) == 1:
    print(len(s)*k//2)
    sys.exit()
for i in s[1:]:
    if start == i:
        seq += 1
    else:
        data.append(seq)
        start = i
        seq = 1
else:
    data.append(seq)
#print(data)
if s[0] != s[-1]:
    ans = 0
    for i in data:
        ans += i//2
    else:
        print(ans*k)
else:
    pati = data[0] + data[-1]
    ans = pati//2*(k-1)
    for i in range(1,len(data)-1):
        ans += data[i]//2*k
    else:
        print(ans+data[0]//2+data[-1]//2)