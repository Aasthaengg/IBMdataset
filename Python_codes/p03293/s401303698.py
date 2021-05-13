s = input()
t = input()

for i in range(len(s)):
    S = s[-(i+1):]+s
    if S[:len(s)] == t:
        print('Yes')
        exit()
    
print('No')