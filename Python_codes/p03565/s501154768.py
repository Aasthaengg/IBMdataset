S = input()
A = input()

if len(S) < len(A):
    print('UNRESTORABLE')
    exit(0)


for i in reversed(range(len(S)-len(A)+1)):
    for j in range(len(A)):
        if not(S[i+j] == A[j] or S[i+j] == '?'):
            break
    else:
        ans = S[:i] + A + S[i+len(A):]
        ans = ans.replace('?', 'a')
        print(ans)
        break
else:
    print('UNRESTORABLE')
