import sys
s = input()
t = input()
num0, num1 = len(s), len(t)

if num0 < num1:
    print('UNRESTORABLE')
elif num0 == num1:
    for i, j in zip(s, t):
        if i != j and i != '?':
            print('UNRESTORABLE')
            sys.exit()
    print(t)
else:
    for i in range(num0-num1, 0, -1):
        for j in range(num1):
            if s[i+j] != t[j] and s[i+j] != '?':
                break
            elif j == num1-1:
                ans = s[:i]+t+s[i+num1:]
                ans = ans.replace('?', 'a')
                print(ans)
                sys.exit()
    print('UNRESTORABLE')
        
            
