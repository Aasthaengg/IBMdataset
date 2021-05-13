S=list(input())
N=len(S)
answers=[0 for _ in range(N)]
numbers_R=[0 for _ in range(N)]
number=0
for n in range(N-1):
    if S[n]=='R':
        number+=1
        if S[n+1]=='L':
            answers[n+1]+=number//2
            answers[n]+=number-number//2
    else:
        number=0
reverse_S=list(reversed(S))
number=0
reverse_answers=list(reversed(answers))
for n in range(N-1):
    if reverse_S[n]=='L':
        number+=1
        if reverse_S[n+1]=='R':
            reverse_answers[n+1]+=number//2
            reverse_answers[n]+=number-number//2
    else:
        number=0
kotae=list(reversed(reverse_answers))
print(*kotae)
