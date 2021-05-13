n = int(input())
s = input()
#n = 45
#s = "tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"
ans = 0
alphabet = [chr(i) for i in range(97, 97+26)]
def count(i):
    num = 0
    a=list(set(list(s[:i])))
    b=list(set(list(s[i:])))
    for i in alphabet:
        if (i in a) & (i in b):
            num += 1
    return num
for j in range(1,len(s)-1):
    if ans < count(j): ans = count(j)
print(ans)