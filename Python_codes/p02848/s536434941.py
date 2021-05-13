N=int(input())
S=input()
print(*[chr(ord(c)+N-(ord(c)+N-65)//26*26) for c in S],sep='')