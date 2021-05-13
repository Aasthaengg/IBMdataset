N,K,S=map(int,input().split())
answers=[str(S)]*K
answers_=[str(S+1)]*(N-K)
a=' '.join(answers)
b=' '.join(answers_)
if K==0:
    if S==pow(10,9):
        answers_ = ['1'] * (N - K)
        b = ' '.join(answers_)
        c=b
    else:
        c=b
elif S==pow(10,9):
    answers_=['1']*(N-K)
    b = ' '.join(answers_)
    c=a+' '+b
else:
    c = a + ' ' + b
print(c)
