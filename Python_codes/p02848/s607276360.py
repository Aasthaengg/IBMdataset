N = int(input())
S = input().strip()
N = N%26
x = ""
for i in range(len(S)):
    k = ord(S[i])
    j = (k-65+N)%26+65
    x += chr(j)
print(x)