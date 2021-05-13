makeA = lambda c: (ord('z')-ord(c)+1) % 26
s = list(map(makeA,list(input())))
#print(s)
K = int(input())
len_s = len(s)
#print(len_s)
for i in range(len_s-1):
    if s[i] <= K:
        K -= s[i]
        s[i] = 0
        #print(s)
if K > 0:
    s[-1] = (s[-1] + 26 - (K % 26)) % 26
#print(s)
makeS = lambda n: chr((26-n)%26+ord('a'))
print(''.join(list(map(makeS,s))))

