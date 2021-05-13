l = [chr(ord('a')+i) for i in range(26)]
C = str(input())

for i in range(26):
    if C == l[i]:
        print(l[i+1])
        exit()