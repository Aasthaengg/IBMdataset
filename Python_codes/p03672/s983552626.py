s=input()
n=len(s)
for i in range(1,n//2):
    if s[0:(n-2*i)//2] == s[(n-2*i)//2:n-2*i]:
        print(len(s[0:(n-2*i)//2])*2)
        exit()
