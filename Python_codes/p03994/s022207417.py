s = [ord(alph)-97 for alph in input()]
K = int(input())
i = 0
while K > 0 and i < len(s)-1:
    if s[i] != 0 and 26-s[i] <= K:
        K -= 26-s[i]
        s[i] = 0
    else:
        i += 1
s[-1] = (s[-1]+K)%26 
print(*[chr(x+97) for x in s], sep = '')