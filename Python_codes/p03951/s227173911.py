n = int(input()) 
s = input()
t = input()
for i in range(n):
    if s[i:] == t[:n-i]:
        print(n-i+i*2)
        break
else:
    print(2*n)