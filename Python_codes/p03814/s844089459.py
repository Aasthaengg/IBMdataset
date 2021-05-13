S=list(input())
length=len(S)
start=S.index('A')
M=list(reversed(S))
finish=M.index('Z')

print(length-start-finish)