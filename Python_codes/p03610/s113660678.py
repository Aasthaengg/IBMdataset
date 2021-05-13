s = input()

for i in range(0,len(s)):
    if not ((i+1)%2==0):
        print(s[i],end='')