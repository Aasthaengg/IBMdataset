S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

b=S()
pair={'A':'T','C':'G','G':'C','T':'A'}
print(pair[b])
