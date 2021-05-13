N=int(input())
S=input()
print(*[chr((ord(c)-65+N)%26+65) for c in S],sep='')