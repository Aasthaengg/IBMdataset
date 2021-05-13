#print(ord('a')) # 97
abc = ''
for i in range(97 ,97+26):
    abc += chr(i)
#print(abc)

S = input()
K = int(input())
ans = ''
for i,s in enumerate(S):
    if ord(s) > ord('a') and 26 - (ord(s) - ord('a')) <= K and i!=len(S)-1:
        ans += 'a'
        #K -= 26 - (ord(s) - ord('a'))
        K -= 26 - (ord(s) - ord('a'))
        #print(K)

    elif i != len(S)-1:
        ans += s
    else:
        #ans += chr(ord(s) + K%26)
        ans += abc[(ord(s) + K%26-ord('a'))%26]
        #print(ans)

print(ans)