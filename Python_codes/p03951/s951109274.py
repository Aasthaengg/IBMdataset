n=int(input())
s=input()
t=input()

for i in range(n+1):
    #print(s[i:],t[:n-i])
    if s[i:] == t[:n-i]:
        print(n+i)
        exit()