s = list(map(str, input().split()))

for i in range(len(s)):
    st=chr(ord(s[i][0])-32)
    print(st,end="")