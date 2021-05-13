import string

alphabet = string.ascii_lowercase

n = int(input())

def DFS(before,keta):
    num = 0
    if keta == n:
        print(before)
        return
    for i in before:
        num = max(num,alphabet.index(i))
    num += 1
    for j in range(num+1):
        DFS(before+alphabet[j],keta+1)

DFS("a",1)