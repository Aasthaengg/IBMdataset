N = int(input())
Answer = int((1/2)*N*(N+1))
Box = [i for i in range(N+1)]
for i in range(2,N+1):
    Answer += sum(Box[i::i])
print(Answer)