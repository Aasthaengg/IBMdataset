s = input()
k = int(input())

len_s = len(s)
moji = [0]*(len_s)

for i in range(len_s):
    num = 26-(ord(s[i])-ord('a'))
    if num <= k and num != 26:
        moji[i] = 'a'
        k -= num
    else:
        moji[i] = s[i]

     
if k != 0:
    #print(k)
    moji[len_s-1] = chr(ord(moji[len_s-1])+k%26)
        
print(*moji,sep='')