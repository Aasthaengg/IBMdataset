n = int(input())
s = input()
t = input()

if s == t:
    print(n)
else:
    for i in range(0, n):
        
        if s[i:] == t[:n-i]:
            print(n*2 - (n-i) )
            break
    else:
        print(n*2)